import requests
'''
This gets the list of the first 100 male users from the randomuser.me api and prints the result
'''

response = requests.get('https://randomuser.me/api/?results=100&gender=male')

print(response.json())

