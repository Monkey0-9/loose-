import os
import sys
import subprocess
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("=" * 60)
    print("      🚀 LOOSE AI | AUTONOMOUS DEVELOPER SHOWCASE")
    print("=" * 60)
    print("   Mode: FAIL-SAFE MOCK (Zero API Keys Required)")
    print("-" * 60)

def main():
    while True:
        clear_screen()
        print_header()
        print("\n   [1] Launch Premium Portal (Streamlit)")
        print("   [2] Run Tech News Analyst (Agno Starter)")
        print("   [3] Run Finance Agent (Multi-Agent Module)")
        print("   [4] Run Full System Audit")
        print("   [5] Exit")
        
        choice = input("\n   Select an option [1-5]: ").strip()
        
        if choice == "1":
            print("\n   Launching Portal...")
            subprocess.Popen([sys.executable, "-m", "streamlit", "run", "loose_portal.py"])
            print("   📍 Access at: http://localhost:8501")
            time.sleep(2)
        elif choice == "2":
            print("\n   Launching Tech Analyst...")
            # We use loose_mock to ensure it runs without keys
            cmd = f"import loose_mock; loose_mock.initialize_sandbox(); from core_modules.agno_starter.main import main; main()"
            subprocess.run([sys.executable, "-c", cmd])
        elif choice == "3":
            print("\n   Launching Finance Agent...")
            # Finance agent has its own UI
            subprocess.Popen([sys.executable, "-m", "streamlit", "run", "utility_modules/finance_agent/main.py", "--server.port", "8502"])
            print("   📍 Access at: http://localhost:8502")
            time.sleep(2)
        elif choice == "4":
            print("\n   Running Audit...")
            subprocess.run([sys.executable, "verify_loose_ai_full.py"])
            input("\n   Press Enter to return to menu...")
        elif choice == "5":
            print("\n   Goodbye! 👋")
            break
        else:
            print("\n   Invalid choice. Try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()
