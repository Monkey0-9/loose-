import json
import os
from datetime import datetime
from pathlib import Path


LOG_FILE = Path(__file__).parent / "telemetry.json"


def log_event(module, level, message):
    """Log a cross-language telemetry event."""
    event = {
        "timestamp": datetime.now().isoformat(),
        "module": module,
        "level": level,
        "message": message,
        "pid": os.getpid()
    }

    # Simple append-only JSON line log
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")


if __name__ == "__main__":
    log_event("telemetry_core", "INFO", "Unified Telemetry System Initialized.")
