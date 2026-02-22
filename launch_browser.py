"""Launch Placement Readiness Platform in the default browser."""
import http.server
import socketserver
import webbrowser
import threading
import time
import os

PORT = 8765
DIR = os.path.join(os.path.dirname(__file__), "static")
URL = f"http://localhost:{PORT}/"

def serve():
    os.chdir(DIR)
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        httpd.serve_forever()

if __name__ == "__main__":
    server = threading.Thread(target=serve, daemon=True)
    server.start()
    time.sleep(0.5)
    webbrowser.open(URL)
    print(f"Placement Readiness Platform opened at {URL}")
    print("Press Ctrl+C to stop the server.")
    try:
        server.join()
    except KeyboardInterrupt:
        pass
