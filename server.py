#!/usr/bin/python

import http.server
#import CGIHTTPServer
import cgitb; cgitb.enable()

server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
server_address = ("", 8000)
handler.cgi_directories = ["/"]

httpd = server(server_address, handler)
httpd.serve_forever()
