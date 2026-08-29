from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import urllib.request

PORT = int(os.environ.get("PORT", 8080))
DB_HOST = os.environ.get("DB_HOST", "postgres-db")
REDIS_HOST = os.environ.get("REDIS_HOST", "redis-cache")

class MultiTierHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response = {
                "status": "healthy",
                "service": "cloud-backend-api",
                "database_target": DB_HOST,
                "cache_target": REDIS_HOST,
                "version": "2.0.0"
            }
            self.wfile.write(json.dumps(response).encode("utf-8"))
        elif self.path == "/api/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response = {
                "message": "Data retrieved successfully",
                "environment": "Docker-Compose Network",
                "infrastructure_components": ["API Gateway", "PostgreSQL", "Redis"]
            }
            self.wfile.write(json.dumps(response).encode("utf-8"))
        else:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response = {"message": "Cloud Multi-Tier API is operational."}
            self.wfile.write(json.dumps(response).encode("utf-8"))

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", PORT), MultiTierHandler)
    print(f"Server starting on port {PORT} connecting to {DB_HOST} & {REDIS_HOST}...")
    server.serve_forever()
