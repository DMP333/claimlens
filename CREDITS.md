# Credits and attribution

ClaimLens is built on open data, open models, and open-source libraries. This file attributes them.

## Source APIs

- [**Google Fact Check Tools API**](https://toolbox.google.com/factcheck/apis)
- [**Wikipedia API**](https://www.mediawiki.org/wiki/API:Main_page) (MediaWiki). Article content is licensed CC BY-SA.
- [**Semantic Scholar API**](https://www.semanticscholar.org/product/api)
- [**OpenAlex API**](https://openalex.org/). Data is licensed CC0.
- **DuckDuckGo**, accessed through the [ddgs](https://github.com/deedy5/ddgs) library.

## Credibility scoring

- **Media Bias/Fact Check dataset**, via [idiap/Factual-Reporting-and-Political-Bias-Web-Interactions](https://github.com/idiap/Factual-Reporting-and-Political-Bias-Web-Interactions) (Apache-2.0). Paper: Sanchez-Cortes et al., "Mapping the Media Landscape: Predicting Factual Reporting and Political Bias Through Web Interactions," CLEF 2024.
- **Open PageRank** by [DomCop](https://www.domcop.com/openpagerank/what-is-openpagerank), used for domain authority scoring.

## Models

- **Stance detection (NLI).** The base model is [MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli](https://huggingface.co/MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli) (MIT license), a DeBERTa-v3-large fine-tuned on MNLI, FEVER-NLI, ANLI, LingNLI, and WANLI. A project-specific LoRA adapter, trained for ClaimLens, is loaded on top of this base at runtime. Please cite Laurer, M., van Atteveldt, W., Salleras Casas, A., and Welbers, K.
- **Relevance and embeddings.** [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) (Apache-2.0), used to score claim-to-source relevance by cosine similarity.

## Core libraries

FastAPI, Uvicorn, httpx, and Pydantic for the web and API layer; PyTorch, Hugging Face Transformers, PEFT, sentence-transformers, scikit-learn, and NLTK for the ML and NLP work; trafilatura and ddgs for retrieval and content extraction; SQLAlchemy and asyncpg for the database. Pinned versions are in `requirements.txt`.