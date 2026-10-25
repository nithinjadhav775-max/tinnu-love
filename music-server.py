from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

class Handler(SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, format, *args):
        print("%s - %s" % (self.address_string(), format % args))

    def copyfile(self, source, outputfile):
        try:
            super().copyfile(source, outputfile)
        except (BrokenPipeError, ConnectionResetError):
            pass

server = ThreadingHTTPServer(("127.0.0.1", 8081), Handler)

print("❤️ Tinnu Love server running")
print("🌐 http://127.0.0.1:8081/memories.html")
print("🎵 http://127.0.0.1:8081/love-song.mp3")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
    server.server_close()
