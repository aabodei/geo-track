import socket
import json
import urllib.request
import tkinter

host_name = socket.gethostbyname(socket.gethostname())
print('IPv4: ' + host_name)

external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
api_url = 'http://api.ipstack.com/' + external_ip + '?access_key=???'


print('Public IP: ' + external_ip)

parameters = ['region_name', 'city', 'latitude', 'longitude']

with urllib.request.urlopen(api_url) as response:
	data = json.load(response)

	for out in parameters:
		out_str = str(out)
		print(out_str + ': ' + str(data[out_str]))
