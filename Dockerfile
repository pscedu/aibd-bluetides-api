FROM python:3.8-slim AS builder

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN python -m venv /venv
ENV PATH=/venv/bin:$PATH

COPY requirements.txt .
# bigfile==0.1.51 is an sdist whose setup.py imports numpy and Cython at build
# time, so both must already be importable before requirements.txt is installed.
# The pre-installed numpy MUST be the same version requirements.txt pins
# (currently numpy==1.18.5, from the deployed tree). A different version here
# would be uninstalled again while requirements.txt is installed, and pip does
# not guarantee that happens before bigfile's C extension is compiled -- which
# would build it against one numpy ABI and run it against another.
RUN pip install --no-cache-dir "Cython==0.29.20" "numpy==1.18.5" \
    && pip install --no-cache-dir -r requirements.txt

FROM python:3.8-slim

COPY --from=builder /venv /venv
ENV PATH=/venv/bin:$PATH \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app
COPY . .

EXPOSE 8000

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000", \
     "--workers", "2", "--timeout", "600", "--access-logfile", "-", "api.main:app"]
