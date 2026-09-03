import json
import sys
import time
import urllib.request


def test_health_endpoint(target_ip):
  url = f"http://{target_ip}:8000/health.json"
  start = time.time()
  try:
    with urllib.request.urlopen(url, timeout=5) as res:
      latency = round((time.time() - start) * 1000, 2)
      payload = json.loads(res.read().decode())
      assert res.getcode() == 200, f"Expected 200, got {res.getcode()}"
      assert payload.get("status") == "healthy", "Payload status mismatch"
      print(f"PASS: {url} -> 200 OK ({latency}ms)")
      return True
  except Exception as exc:
    print(f"FAIL: {exc}")
    return False


if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Usage: python3 test_cloud_endpoint.py <IP_ADDRESS>")
    sys.exit(1)
  success = test_health_endpoint(sys.argv[1])
  sys.exit(0 if success else 1)
