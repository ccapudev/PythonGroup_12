import requests

URL_BASE = 'https://api.github.com'

path = lambda x : URL_BASE + x

consulta = requests.get(path('/events'))
print(consulta.url)
print(len(consulta.content))
print(consulta.status_code)
