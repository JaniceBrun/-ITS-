from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
import ssl

# httpd = HTTPServer(("localhost", 1970), BaseHTTPRequestHandler)
# ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
# ctx.load_cert_chain(certfile="./cert.pem", keyfile="./key.pem")
# httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)
# httpd.serve_forever()

#openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365

# httpd = HTTPServer(("localhost", 8000), BaseHTTPRequestHandler)
# httpd.serve_forever()

class MyHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"hello miao")

httpd = HTTPServer(("localhost", 8000), MyHTTPRequestHandler)
httpd.serve_forever()