from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import socket

PORT = int(os.environ.get("PORT", 8080))
DB_HOST = os.environ.get("DB_HOST", "postgres-db")
REDIS_HOST = os.environ.get("REDIS_HOST", "redis-cache")
HOSTNAME = socket.gethostname()

class MultiTierHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response = {
                "status": "healthy",
                "instance_id": HOSTNAME,
                "service": "cloud-backend-api",
                "database_target": DB_HOST,
                "cache_target": REDIS_HOST,
                "version": "2.1.0"
            }
            self.wfile.write(json.dumps(response).encode("utf-8"))
        elif self.path == "/api/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response = {
                "message": "Data served successfully",
                "handled_by_instance": HOSTNAME,
                "infrastructure_components": ["Nginx Proxy", "API Replicas", "PostgreSQL", "Redis"]
            }
            self.wfile.write(json.dumps(response).encode("utf-8"))
        else:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response = {"message": f"Cloud Multi-Tier API running on instance {HOSTNAME}"}
            self.wfile.write(json.dumps(response).encode("utf-8"))

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", PORT), MultiTierHandler)
    print(f"Instance {HOSTNAME} starting on port {PORT}...")
    server.serve_forever()
