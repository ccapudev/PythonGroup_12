import requests


# http://maps.google.com/maps/api/geocode/json
URL_BASE = 'https://maps.google.com'

path = lambda x : URL_BASE + x

template = 'https://www.google.com/maps/@{},{},16z'

params = {
    'key': 'AIzaSyAtHCfkXKqCIBsjkkT05UNzEp91ZVtN71o',
    # 'address': input("Ingrese dirección: ")
    'address': 'tecnicas metalicas ingenieros',
}

consulta = requests.get(path('/maps/api/geocode/json'), params=params)

response = consulta.json()

for r in response.get('results'):
    if r.get('geometry'):
        geometry = r.get('geometry') or {}
        if geometry.get('location'):
            location = geometry.get('location') or {}
            print(template.format(
                location.get('lat'),
                location.get('lng'),
            ))

# print(consulta.url)
# print(consulta.json())
# print(consulta.status_code)
