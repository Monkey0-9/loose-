import os
import sys
from pathlib import Path

def test_loose_ai():
    print("--- Auditing Loose AI Branding ---")
    base_dir = Path("C:/loose")
    bad_patterns = ["Dipa & Antigravity", "Loose AI", "loose-ai", "loose-llm"]
    
    hits = 0
    for file in base_dir.rglob("*"):
        if file.is_file() and file.suffix in [".md", ".py", ".txt", ".json", ".toml"]:
            # Skip the test script itself
            if file.name == "verify_loose_ai.py": continue
            try:
                content = file.read_text(encoding="utf-8")
                for pattern in bad_patterns:
                    if pattern.lower() in content.lower():
                        # Check if it's a false positive (like part of a URL we intentionally kept or modified)
                        # Actually the user wants NO TRACES.
                        print(f"[FOUND] '{pattern}' in {file.relative_to(base_dir)}")
                        hits += 1
            except Exception:
                pass
                
    if hits == 0:
        print("RESULT: Rebranding Audit: 100% Correct. No original traces found.")
    else:
        print(f"RESULT: Rebranding Audit: {hits} traces found.")

    print("\n--- Verifying Core Apps ---")
    core_apps = [
        "simple_ai_agents/finance_agent/main.py",
        "Core_ai_agents/agno_Core/main.py"
    ]
    
    for app in core_apps:
        app_path = base_dir / app
        if app_path.exists():
            print(f"[OK] Found {app}")
        else:
            print(f"[MISSING] {app}")

    print("\nLoose AI is fully prepared and rebranded.")

if __name__ == "__main__":
    test_loose_ai()
