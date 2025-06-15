FROM python:3.11-slim as builder

WORKDIR /app

RUN python -m venv /opt/venv
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
COPY logger.py .
COPY server.py .
COPY read_services.py .
COPY state.py .
COPY main.py .

COPY services.yaml /app/data

RUN pip install --upgrade pip && pip install -r requirements.txt

# Final minimal stage
FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /opt/venv /opt/venv
COPY --from=builder /app /app

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN adduser --disabled-password --gecos '' --uid 1000 appuser && \
    chown -R appuser:appuser /app /opt/venv

USER appuser

CMD ["python", "main.py"]