import os
import http.server
import socketserver

from http import HTTPStatus


class Handler(SimpleHTTPRequestHandler):
  def do_GET(self):
    self.send_response(HTTPStatus.MOVED_PERMANENTLY)
    self.send_header('Location', 'https://chrisdayberry.kw.com/')  # Replace with your target URL
    self.end_headers()


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
