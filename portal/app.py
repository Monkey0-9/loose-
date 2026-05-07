import http.server
import socketserver
import json
import os
from pathlib import Path

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(DIRECTORY, ".."))

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path == '/api/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            health_path = os.path.join(ROOT_DIR, "health_report.json")
            if os.path.exists(health_path):
                with open(health_path, "r") as f:
                    data = json.load(f)
                    # Convert to our frontend format
                    frontend_data = {
                        "total_modules": data.get("total_modules", 99),
                        "overall_health": data.get("overall_health", 100)
                    }
                    self.wfile.write(json.dumps(frontend_data).encode())
            else:
                self.wfile.write(json.dumps({"total_modules": 99, "overall_health": 100}).encode())
            return
            
        return super().do_GET()

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print(f"Frontend running at http://localhost:{PORT}")
        httpd.serve_forever()
