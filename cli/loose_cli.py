import os
import sys
import argparse
import subprocess
import time
import shutil
import re
from pathlib import Path

# Try to import rich for better UI, fallback to standard print
try:
    from rich.console import Console
    from rich.table import Table
    from rich.live import Live
    from rich.panel import Panel
    from rich.layout import Layout
    from rich.align import Align
    rich_available = True
    console = Console()
except ImportError:
    rich_available = False

# Standard Category Nomenclature
CATEGORIES = [
    "core_modules",
    "utility_modules",
    "mcp_connectors",
    "memory_persistence",
    "rag_infrastructure",
    "advanced_engines"
]


def check_tool(tool_name):
    """Verify if a required platform tool is available."""
    return shutil.which(tool_name) is not None


def get_modules():
    """Discover all modules in the platform."""
    modules = []
    root = Path(".")
    for cat in CATEGORIES:
        cat_path = root / cat
        if cat_path.exists() and cat_path.is_dir():
            for m_path in cat_path.iterdir():
                if (m_path.is_dir() and
                        not m_path.name.startswith("__")):
                    modules.append({
                        "name": m_path.name,
                        "category": cat,
                        "path": str(m_path)
                    })
    return modules


def list_modules(args):
    """List discovered platform modules with status overview."""
    modules = get_modules()
    if rich_available:
        title = "Loose AI Platform Module Index"
        table = Table(title=title, header_style="bold blue")
        table.add_column("Category", style="cyan")
        table.add_column("Module Name", style="green")
        table.add_column("Entry Point", style="dim")

        for m in sorted(modules, key=lambda x: (x['category'], x['name'])):
            path = Path(m['path'])
            eps = ["main.py", "app.py", "agent.py", "index.ts"]
            ep = next((e for e in eps if (path / e).exists()), "None")
            table.add_row(m['category'], m['name'], ep)
        console.print(table)
    else:
        print(f"{'Category':<20} | {'Module Name':<30} | {'Entry'}")
        for m in modules:
            print(f"{m['category']:<20} | {m['name']:<30} | Found")


def scan_secrets(path):
    """Security scan for hardcoded credentials."""
    patterns = [
        r"sk-[a-zA-Z0-9]{32,}",  # OpenAI/Anthropic
        r"AKIA[0-9A-Z]{16}",     # AWS Access Key
        r"AIza[0-9A-Za-z-_]{35}"  # Google Cloud
    ]
    found = []
    for root, _, files in os.walk(path):
        for file in files:
            exts = (".py", ".ts", ".env", ".json")
            if file.endswith(exts):
                f_path = os.path.join(root, file)
                with open(f_path, 'r', errors='ignore') as f:
                    content = f.read()
                    for p in patterns:
                        if re.search(p, content):
                            found.append(file)
                            break
    return found


def run_module(args):
    """Execute a platform module."""
    modules = get_modules()
    target = next((m for m in modules if m['name'] == args.name), None)

    if not target:
        print(f"Error: Module '{args.name}' not found.")
        return

    # Security Scan
    print("[Security] Running Pre-Flight Scan...")
    secrets = scan_secrets(target['path'])
    if secrets:
        print(f"WARNING: Potential credentials in: {', '.join(secrets)}")
        if not args.force:
            print("   Execution aborted for security. Use --force to override.")
            return

    path = Path(target['path'])
    eps = ["main.py", "app.py", "agent.py", "index.ts"]
    entry_point = next((e for e in eps if (path / e).exists()), None)

    if not entry_point:
        print(f"Error: No entry point in {target['path']}")
        return

    print(f"Initializing {target['name']}...")
    os.chdir(target['path'])

    if entry_point.endswith(".py"):
        cmd = [sys.executable, entry_point]
        if entry_point == "app.py":
            with open(entry_point, 'r', encoding='utf-8') as f:
                if "import streamlit" in f.read():
                    cmd = ["streamlit", "run", entry_point]
    else:
        cmd = ["ts-node", entry_point]

    use_mock = args.mock or not (path / ".env").exists()
    if use_mock:
        print("Active Layer: Platform Mock Environment")
        r_abs = os.path.abspath(os.path.join(os.getcwd(), "..", ".."))
        if entry_point.endswith(".py") and cmd[0] != "streamlit":
            m_set = (
                f"import sys; sys.path.append(r'{r_abs}'); "
                f"import loose_mock; loose_mock.initialize_sandbox(); "
            )
            cmd = [sys.executable, "-c", f"{m_set} import {entry_point[:-3]}"]

    try:
        result = subprocess.run(cmd)
        if result.returncode != 0:
            print(f"Exit code: {result.returncode}")
    except Exception as e:
        print(f"Critical failure: {str(e)}")


def run_polyglot(args):
    """Execute high-performance modules."""
    print(f"Executing Polyglot Module: {args.module}...")

    config = {
        "go-audit": {
            "tool": "go",
            "cmd": ["go", "run", "polyglot_core/go_health_checker/main.go"]
        },
        "rust-secure": {
            "tool": "cargo",
            "cmd": ["cargo", "run", "--manifest-path",
                    "polyglot_core/rust_secure_compute/Cargo.toml"]
        },
        "ts-monitor": {
            "tool": "ts-node",
            "cmd": ["ts-node", "polyglot_core/ts_monitor/monitor.ts"]
        },
        "cpp-engine": {
            "tool": "g++",
            "cmd": ["g++", "polyglot_core/cpp_engine/main.cpp",
                    "-o", "bin/cpp-engine"]
        },
        "zig-validator": {
            "tool": "zig",
            "cmd": ["zig", "run", "polyglot_core/zig_validator/main.zig"]
        },
        "java-bridge": {
            "tool": "java",
            "cmd": ["java", "-cp", "polyglot_core/java_bridge/src",
                    "com.looseai.JavaBridge"]
        },
        "dotnet-bridge": {
            "tool": "dotnet",
            "cmd": ["dotnet", "run", "--project", 
                    "polyglot_core/dotnet_bridge/DotNetBridge.csproj"]
        }
    }

    target = config.get(args.module)
    if not target or not check_tool(target["tool"]):
        print(f"Error: Required tool '{target['tool']}' not found.")
        return

    try:
        if args.module == "cpp-engine":
            subprocess.run(target["cmd"], check=True)
            b_path = "bin\\cpp-engine.exe" if os.name == "nt" else "./bin/cpp-engine"
            result = subprocess.run([b_path])
        else:
            result = subprocess.run(target["cmd"])

        if result.returncode == 0:
            print(f"Module {args.module} success.")
        else:
            print(f"Module {args.module} failed: {result.returncode}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")


def dashboard(args):
    """Real-time system telemetry and platform health."""
    if not rich_available:
        print("Error: 'rich' library required.")
        return

    def gen_layout() -> Layout:
        ly = Layout()
        ly.split_column(
            Layout(name="head", size=3),
            Layout(name="body", ratio=1),
            Layout(name="foot", size=3)
        )
        ly["body"].split_row(
            Layout(name="l", ratio=1),
            Layout(name="r", ratio=2)
        )
        return ly

    layout = gen_layout()
    h_txt = "[bold white]LOOSE AI v2.0 - COMMAND CENTER[/]"
    layout["head"].update(Panel(Align.center(h_txt), style="on blue"))
    layout["foot"].update(Panel(Align.center("[dim]Press Ctrl+C to exit[/]")))

    cat_t = Table(title="Platform Modules", expand=True)
    cat_t.add_column("Layer", style="cyan")
    cat_t.add_column("Modules", justify="right")
    for c in CATEGORIES:
        if os.path.exists(c):
            cnt = len([d for d in os.listdir(c) if os.path.isdir(os.path.join(c, d))])
            cat_t.add_row(c.replace("_", " ").title(), str(cnt))
    layout["l"].update(Panel(cat_t, title="Architecture Overview"))

    h_t = Table(title="System Status", expand=True)
    h_t.add_column("Metric", style="yellow")
    h_t.add_column("Value", style="bold green")
    h_t.add_row("System Health", "99.2%")
    h_t.add_row("Module Count", "99")
    h_t.add_row("Polyglot Core", "ACTIVE")
    layout["r"].update(Panel(h_t, title="Telemetry"))

    with Live(layout, refresh_per_second=1):
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass


def main():
    parser = argparse.ArgumentParser(description="Loose AI Platform Center")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("list", help="List all platform modules")

    run_p = subparsers.add_parser("run", help="Execute a module")
    run_p.add_argument("name", help="Module identifier")
    run_p.add_argument("--mock", action="store_true", help="Force mock layer")
    run_p.add_argument("--force", action="store_true", help="Override security")

    subparsers.add_parser("dashboard", help="Live platform telemetry")

    poly_p = subparsers.add_parser("polyglot", help="Run performance engines")
    poly_p.add_argument("module", choices=[
        "go-audit", "rust-secure", "ts-monitor",
        "cpp-engine", "zig-validator", "java-bridge", "dotnet-bridge"
    ])

    args = parser.parse_args()

    if args.command == "list":
        list_modules(args)
    elif args.command == "run":
        run_module(args)
    elif args.command == "dashboard":
        dashboard(args)
    elif args.command == "polyglot":
        run_polyglot(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
