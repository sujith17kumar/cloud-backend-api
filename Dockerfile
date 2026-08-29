# Stage 1: Build Stage
FROM python:3.11-slim AS builder
WORKDIR /app
COPY app.py .

# Stage 2: Final Runtime Stage
FROM python:3.11-alpine
WORKDIR /app

# Non-root security user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Copy app code
COPY --from=builder /app/app.py .

USER appuser
EXPOSE 8080

# Reliable native Python healthcheck
HEALTHCHECK --interval=10s --timeout=3s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/health')" || exit 1

CMD ["python", "app.py"]

