# Slim Debian + Python 3.11. The slim base stays small; what makes this image
# large is torch + the baked-in models, which is expected and accepted.
FROM python:3.11-slim

# PYTHONUNBUFFERED: logs flush immediately so `docker logs` shows prints live.
# PYTHONDONTWRITEBYTECODE: no .pyc clutter baked into the image.
# HF_HOME / NLTK_DATA: fixed cache paths so models downloaded at BUILD time land
# exactly where the app looks for them at RUN time.
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    HF_HOME=/opt/models/hf \
    NLTK_DATA=/opt/models/nltk

WORKDIR /app

# --- Dependencies: the expensive, rarely-changing layer. Copy ONLY requirements
# first, so editing app code later does not invalidate this layer. ---
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# --- Bake the models in: also expensive and rarely-changing. Pre-download the
# two Hub models and the NLTK data INTO the image (into HF_HOME / NLTK_DATA) so
# the running container never reaches the network for them. ---
RUN python -c "from transformers import AutoTokenizer, AutoModelForSequenceClassification; m='MoritzLaurer/deberta-v3-large-mnli-fever-anli-ling-wanli'; AutoTokenizer.from_pretrained(m); AutoModelForSequenceClassification.from_pretrained(m)" \
    && python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')" \
    && python -c "import nltk; [nltk.download(p) for p in ('punkt_tab','averaged_perceptron_tagger_eng','averaged_perceptron_tagger')]"

# From here on the models are present, so force offline mode: the container will
# load them from the local cache and never phone home at runtime. (Set AFTER the
# download step above, or it would block the download itself.)
ENV HF_HUB_OFFLINE=1 \
    TRANSFORMERS_OFFLINE=1

# --- Your fine-tuned LoRA adapter: local, must be copied. Loaded on top of the
# base model at runtime. Separate COPY so it caches independently of app code. ---
COPY finetune/ ./finetune/

# --- App code: the cheap, frequently-changing layer, copied last so edits only
# rebuild from here down. ---
COPY app/ ./app/

# Documents the port the app serves on (publishing happens in compose).
EXPOSE 8000

# 0.0.0.0 (not localhost) so the published port can reach uvicorn inside the
# container. No --reload: that is a dev-only convenience, not for a built image.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]