"""Retry logic for failed webhook deliveries."""

MAX_ATTEMPTS = 5
TIMEOUT_SECONDS = 30

def retry_with_backoff(fn):
    for attempt in range(MAX_ATTEMPTS):
        try:
            return fn(timeout=TIMEOUT_SECONDS)
        except Exception:
            wait = 2 ** attempt
            sleep(wait)
    raise RuntimeError("max retries exceeded")
