import requests

#url = 'http://www.gmit.ie'

#response = requests.get(url)

#print(response.status_code)
#print(response.text)
#print(response.headers)

url = 'http://127.0.0.1:5000/cars'
data = {'reg':'123', 'make': 'blah', 'model': 'blah', 'price': 123}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())