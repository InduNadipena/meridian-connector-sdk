# meridian-connector-sdk

SDK powering Project Meridian's connector framework — supports both Knowledge connectors
(index-based) and Tools connectors (live API calls). See src/sync_pipeline.py for the
ingestion pipeline and src/retry.py for the shared retry/backoff logic used by every
connector.
