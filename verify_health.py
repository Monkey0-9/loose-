import json
from pathlib import Path
from datetime import datetime

# Custom Architectural Tiers
CATEGORIES = [
    "core_modules",
    "utility_modules",
    "mcp_connectors",
    "memory_persistence",
    "rag_infrastructure",
    "advanced_engines"
]

def verify_module(module):
    """Perform structural integrity audit on a platform module."""
    path = Path(module['path'])
    
    # 1. Entry Point Detection
    entry_points = ["main.py", "app.py", "agent.py", "index.ts"]
    has_entry = any((path / ep).exists() for ep in entry_points)
    
    if not has_entry:
        return "ERROR: No entry point detected"
    
    # 2. Configuration Integrity
    has_env = (path / ".env.example").exists() or (path / ".env").exists()
    if not has_env:
        return "WARNING: Configuration schema missing"
        
    return "HEALTHY"

def run_audit():
    """Execute global platform health audit."""
    print("Loose AI - Platform Integrity Audit")
    print("Auditing custom architectural tiers...")
    
    report = {
        "timestamp": datetime.now().isoformat(),
        "summary": {"total_modules": 0, "healthy_modules": 0, "categories": {}},
        "details": []
    }
    
    for cat in CATEGORIES:
        cat_path = Path(cat)
        cat_stats = {"total": 0, "healthy": 0}
        
        if cat_path.exists():
            for m_dir in cat_path.iterdir():
                if m_dir.is_dir() and not m_dir.name.startswith("__"):
                    m_info = {"name": m_dir.name, "category": cat, "path": str(m_dir)}
                    status = verify_module(m_info)
                    
                    m_info["status"] = status
                    report["details"].append(m_info)
                    
                    cat_stats["total"] += 1
                    report["summary"]["total_modules"] += 1
                    if status == "HEALTHY":
                        cat_stats["healthy"] += 1
                        report["summary"]["healthy_modules"] += 1
                        
        report["summary"]["categories"][cat] = cat_stats

    with open("health_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)
        
    print(f"\nAudit Complete. {report['summary']['total_modules']} modules processed.")
    print("Platform integrity report saved to health_report.json")

if __name__ == "__main__":
    run_audit()
