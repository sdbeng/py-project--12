from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

class webServerHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        try:
            if self.path.endswith("/restaurants"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>restaurants list </body></html>"
                self.wfile.write(output.encode())
                print(output.encode())
                return
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


def main():
    try:
        port = 8000
        server = HTTPServer(('', port), webServerHandler)
        print("Web Server - restaurants - running on port %s" % port)
        server.serve_forever()
    except KeyboardInterrupt:
        print(" ^C entered, stopping web server...")
        server.socket.close()


if __name__ == '__main__':
    main()