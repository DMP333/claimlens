import httpx
from app.models.schemas import Source, ClaimRequest

WIKIDATA_URL = "https://www.wikidata.org/w/api.php"

STOP_WORDS = {
    "is", "was", "were", "are", "the", "a", "an", "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "that", "this", "it", "not", "and", "or", "but",
    "has", "had", "have", "be", "been", "being", "do", "does", "did", "will",
    "would", "could", "should", "can", "may", "might", "than", "more", "less",
    "also", "just", "about", "into", "over", "after", "before", "between",
    "through", "during", "without", "because", "if", "when", "where", "how",
    "what", "which", "who", "whom", "there", "here", "then", "so", "no", "yes",
    "all", "each", "every", "both", "few", "some", "any", "most", "other",
    "such", "only", "same", "its", "very", "up", "out",
}

KEY_PROPERTIES = {
    "P31": "instance of",
    "P17": "country",
    "P27": "country of citizenship",
    "P19": "place of birth",
    "P20": "place of death",
    "P569": "date of birth",
    "P570": "date of death",
    "P106": "occupation",
    "P36": "capital",
    "P1082": "population",
    "P6": "head of government",
    "P35": "head of state",
    "P131": "located in",
    "P571": "inception",
    "P576": "dissolved",
    "P112": "founded by",
    "P159": "headquarters location",
}

#TODO: explore different parameter options for api
#TODO: consider parallelizing entity searches with asyncio.gather


async def search_wikidata(claim_request: ClaimRequest) -> list[Source]:
    search_terms = _extract_search_terms(claim_request.claim)
    if not search_terms:
        return []

    entity_ids = []
    entity_labels = {}

    async with httpx.AsyncClient(headers={"User-Agent": "FalseClaimDetector/1.0 (minwoopark.333@gmail.com)"}) as client:
        # Step 1: search for entities matching each extracted term
        for term in search_terms:
            params = {
                "action": "wbsearchentities",
                "search": term,
                "language": "en",
                "format": "json",
                "limit": 3,
                "type": "item",
            }
            response = await client.get(WIKIDATA_URL, params=params)
            if response.status_code != 200:
                continue

            for item in response.json().get("search", []):
                eid = item.get("id")
                if eid and eid not in entity_labels:
                    entity_ids.append(eid)
                    entity_labels[eid] = item.get("label", eid)

        if not entity_ids:
            return []

        # Step 2: fetch properties for all found entities in one batch call
        detail_response = await client.get(WIKIDATA_URL, params={
            "action": "wbgetentities",
            "ids": "|".join(entity_ids[:10]),
            "languages": "en",
            "format": "json",
            "props": "descriptions|claims|labels",
        })

        if detail_response.status_code != 200:
            return []

        entities = detail_response.json().get("entities", {})

        # Collect all Q-codes from property values that need label resolution
        q_codes_to_resolve = set()
        for entity in entities.values():
            claims_data = entity.get("claims", {})
            for prop_id in KEY_PROPERTIES:
                if prop_id in claims_data:
                    for claim in claims_data[prop_id][:2]:
                        datavalue = claim.get("mainsnak", {}).get("datavalue", {})
                        if datavalue.get("type") == "wikibase-entityid":
                            qid = datavalue.get("value", {}).get("id")
                            if qid:
                                q_codes_to_resolve.add(qid)

        # Step 3: batch resolve Q-codes to human-readable labels
        resolved_labels = {}
        if q_codes_to_resolve:
            resolve_response = await client.get(WIKIDATA_URL, params={
                "action": "wbgetentities",
                "ids": "|".join(list(q_codes_to_resolve)[:50]),
                "languages": "en",
                "format": "json",
                "props": "labels",
            })
            if resolve_response.status_code == 200:
                for qid, qentity in resolve_response.json().get("entities", {}).items():
                    resolved_labels[qid] = (
                        qentity.get("labels", {}).get("en", {}).get("value", qid)
                    )

    # Step 4: build Source objects with readable snippets
    sources = []
    for entity_id in entity_ids[:10]:
        if entity_id not in entities:
            continue

        entity = entities[entity_id]
        label = entity.get("labels", {}).get("en", {}).get("value", entity_id)
        description = entity.get("descriptions", {}).get("en", {}).get("value", "")
        claims_data = entity.get("claims", {})

        facts = []
        for prop_id, prop_label in KEY_PROPERTIES.items():
            if prop_id not in claims_data:
                continue
            for claim in claims_data[prop_id][:1]:
                datavalue = claim.get("mainsnak", {}).get("datavalue", {})
                value_type = datavalue.get("type")

                if value_type == "wikibase-entityid":
                    qid = datavalue.get("value", {}).get("id")
                    value_str = resolved_labels.get(qid, qid)
                elif value_type == "time":
                    value_str = _parse_time(datavalue.get("value", {}).get("time", ""))
                elif value_type == "quantity":
                    value_str = datavalue.get("value", {}).get("amount", "").lstrip("+")
                elif value_type == "string":
                    value_str = datavalue.get("value", "")
                else:
                    continue

                facts.append(f"{prop_label}: {value_str}")

        snippet_parts = [description] if description else []
        snippet_parts.extend(facts)
        snippet = " | ".join(snippet_parts) if snippet_parts else label

        source = Source(
            url=f"https://www.wikidata.org/wiki/{entity_id}",
            title=label,
            snippet=snippet,
            source_type="knowledge_graph",
            raw_claim_rating=None,
        )
        sources.append(source)

    return sources


def _extract_search_terms(claim: str) -> list[str]:
    words = claim.split()
    chunks = []
    current_chunk = []

    for word in words:
        clean = word.strip(".,!?;:'\"()[]").lower()
        if clean in STOP_WORDS:
            if current_chunk:
                chunks.append(" ".join(current_chunk))
                current_chunk = []
        else:
            current_chunk.append(word.strip(".,!?;:'\"()[]"))

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return [c for c in chunks if len(c) > 1][:3]


def _parse_time(time_str: str) -> str:
    try:
        clean = time_str.lstrip("+-")
        date_part = clean.split("T")[0]
        year, month, day = date_part.split("-")
        months = [
            "", "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December",
        ]
        month_idx = int(month)
        if 1 <= month_idx <= 12:
            return f"{months[month_idx]} {int(day)}, {year}"
        return date_part
    except (ValueError, IndexError):
        return time_str