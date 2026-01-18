import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()

        message = "Lab2 container is running\n"
        self.wfile.write(message.encode("utf-8"))


def main():
    host = "0.0.0.0"
    port = int(os.environ.get("PORT", "8080"))

    httpd = HTTPServer((host, port), Handler)
    print(f"Listening on http://{host}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    main()
