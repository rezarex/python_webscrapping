'''
More code on using requests library
'''

import requests

response = requests.get("https://httpbin.org/get")

#print(response.status_code)
#print(response.json())
res_json = response.json()
#del res_json['origin']
#print(res_json) #prints response without the origin host IP address
#print(response.text) #prints the whole response
#print(response.url) #prints the requested URL
