#!/usr/bin/python

import sys
import cgitb; cgitb.enable()

if sys.version_info[0]<3:
    import BaseHTTPServer
    import CGIHTTPServer

    server = BaseHTTPServer.HTTPServer
    handler = CGIHTTPServer.CGIHTTPRequestHandler

else:
    import http.server

    server = http.server.HTTPServer
    handler = http.server.CGIHTTPRequestHandler
    
server_address = ("", 8000)
handler.cgi_directories = ["/"]

httpd = server(server_address, handler)
httpd.serve_forever()
