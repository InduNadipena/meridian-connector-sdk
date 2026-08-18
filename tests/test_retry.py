"""Tests for retry_with_backoff."""
import pytest
from src.retry import retry_with_backoff, MAX_ATTEMPTS

def test_max_attempts_is_three():
    assert MAX_ATTEMPTS == 3

def test_succeeds_on_first_try():
    calls = []
    def fn():
        calls.append(1)
        return "ok"
    assert retry_with_backoff(fn) == "ok"
    assert len(calls) == 1
