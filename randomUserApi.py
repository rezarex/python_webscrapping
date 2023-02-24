import requests
'''
This gets the list of the first 100 male users from the randomuser.me api and prints the result
'''
#first method passes params at the end of the line
#response = requests.get('https://randomuser.me/api/?results=100&gender=male')

#but we could pass params instead of adding them at the end of the line..
params = {
    'gender': 'male', 
    'results':100
    }
response = requests.get('https://randomuser.me/api/', params=params)

print(response.json())
#print(response.url) #--> shows the resulting url

