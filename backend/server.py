import os, json
from http.server import HTTPServer, SimpleHTTPRequestHandler
import urllib.parse

PORT = 8000
DATA_PATH = os.path.join(os.path.dirname(__file__), 'app', 'data', 'synthetic_orders.json')

def get_orders():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

class PratyarpanHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        if path == '/api/orders':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(get_orders()).encode('utf-8'))
        elif path == '/api/health' or path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'OPERATIONAL', 'portal': 'GeM Pratyarpan'}).encode('utf-8'))
        else:
            super().do_GET()

if __name__ == '__main__':
    httpd = HTTPServer(('', PORT), PratyarpanHandler)
    print(f'Server running at http://localhost:{PORT}')
    httpd.serve_forever()
