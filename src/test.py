import requests


#payload = {'key1': 'value1', 'key2': 'value2'}  
#r = requests.get('https://httpbin.org/get', params=payload)
#r = requests.get('https://api.github.com/events')
#r.text
r = requests.get('https://api.github.com/events')
r.json()
print(r.status_code)