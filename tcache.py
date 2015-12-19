#!/usr/bin/env python3
import time
import http.server
import requests

HOST_NAME 	= ''
PORT 		= 8000
# Twit.tv Info:
API_URL 	= "https://twit.tv/api/v1.0/"
APP_ID 		= ""
APP_KEY 	= ""

class Cache():
	'''Simple cache using a dictionary. If the URL is not stored, the JSON
	is fetched using requests.get().'''
	def __init__(self):
		print("Creating empty cache")
		self.cache = dict()

	def __contains__(self, url):
		return url in self.cache

	def define(self, url, value):
		self.cache[url] = value

	def get(self, url):
		return self.cache[url]

	def getData(self, url):
		print(url[len(API_URL):], end=' ')
		if url not in cache:
			data = self.getURL(url)
			if data == None:
				return ""
			self.define(url, data)
		else:
			print('In cache')
		return self.get(url)

	def getURL(self, url):
		headers = {'app-id': APP_ID , 'app-key': APP_KEY}
		r = requests.get(url, headers=headers)
		print(r.status_code)
		if r.status_code == 200:
			return r.text
		return None


class MyHandler(http.server.BaseHTTPRequestHandler):
	'''Handles requests from an HTTPServer and uses a cache to fulfill 
	requests.'''
	global cache
	def do_HEAD(self):
		self.send_response(200)
		self.end_headers()

	def do_GET(self):
		''' Respond to a GET request.'''
		self.send_response(200)
		self.send_header("Content-type", "text/json")
		self.end_headers()

		url = API_URL + self.path[1:]
		self.writeMessage(str(cache.getData(url)))

	def EncodeMessage(self, msg):
		'''Encodes a string using UTF-8. (Necessary to write to wfile.)'''
		return bytes(str(msg), "UTF-8")

	def writeMessage(self, msg):
		'''Helper function that takes a string, encodes it and writes it to 
		wfile.'''
		self.wfile.write(self.EncodeMessage(msg))

	def log_request(self, format, *args):
		'''Disabling HTTPServer's messages.'''
		return


if __name__ == '__main__':
	# Creating a cache instance:
	cache = Cache()
	# Creating an HTTP server instance that uses the MyHandler class:
	httpd = http.server.HTTPServer((HOST_NAME, PORT), MyHandler)

	# Starting the server and listening until CTRL+C...
	print("Listening at port", PORT)
	print(time.asctime(), "-", "Server started")
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
	print(time.asctime(), "-", "Server stopped")