"""Sync pipeline for Project Meridian connectors."""

def ingest(events, mode="batch"):
    """Ingest events in batch or streaming mode."""
    seen = set()
    for event in events:
        dedup_key = event["id"]
        if dedup_key in seen:
            continue  # prevents duplicate sync events on reconnect
        seen.add(dedup_key)
        process(event)

def process(event):
    """Normalize and write a single event to the destination index."""
    normalized = {
        "id": event["id"],
        "type": event.get("type", "unknown"),
        "payload": event.get("payload", {}),
    }
    write_to_index(normalized)

def write_to_index(record):
    """Persist one normalized record to the search index."""
    index.upsert(record["id"], record)
