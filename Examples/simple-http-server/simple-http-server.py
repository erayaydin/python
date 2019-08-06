#!/usr/bin/env python

# http.server paketinden gerekli sınıfların eklenmesi.
from http.server import BaseHTTPRequestHandler, HTTPServer

# Gelen istekleri kontrol edecek sınıfımız
class myServerHandlerClass(BaseHTTPRequestHandler):
	def do_GET(self):
		# Sonuç cevap kodu
		self.send_response(200)

		# Sonuç baslik(header) bilgileri
		self.send_header('Content-type', 'text/html')
		self.end_headers()

		# Sonuç body
		self.wfile.write(bytes("Hello Python Web", "utf8"))
		return

print("Starting server...")
# Yayın yapacağımız adres ve port
# http://localhost:8081 adresinden kontrol edebiliriz.
server_address = ('127.0.0.1', 8081)
httpd = HTTPServer(server_address, myServerHandlerClass)
print("Running server...")
httpd.serve_forever() # Sonsuza kadar çalış :)
