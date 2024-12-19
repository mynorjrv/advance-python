import json
import requests

key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]


def show_head():
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()


def show_empty():
    for w in key_widths:
        print(' '.ljust(w), end='| ')
    print()


def show_car(car):
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end='| ')
    print()


def show(json):
    show_head()
    if type(json) is list:
        for car in json:
            show_car(car)
    elif type(json) is dict:
        if json:
            show_car(json)
        else:
            show_empty()

# Deleting car with id 1
headers = {'Connection': 'Close'}
try:
    reply = requests.delete('http://localhost:3000/cars/1')
    print("res=" + str(reply.status_code))
    reply = requests.get('http://localhost:3000/cars/', headers=headers)
except requests.RequestException:
    print('Communication error')
else:
    print('Connection=' + reply.headers['Connection'])
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print('Server error')


# Creating car with id 7
h_close = {'Connection': 'Close'}
h_content = {'Content-Type': 'application/json'}
new_car = {
    'id': 7,
    'brand': 'Porsche',
    'model': '911',
    'production_year': 1963,
    'convertible': False
}
print(json.dumps(new_car))
try:
    reply = requests.post(
        'http://localhost:3000/cars', 
        headers=h_content, 
        data=json.dumps(new_car)
    )
    print("reply=" + str(reply.status_code))
    reply = requests.get(
        'http://localhost:3000/cars/', 
        headers=h_close
    )
except requests.RequestException:
    print('Communication error')
else:
    print('Connection=' + reply.headers['Connection'])
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print('Server error')


# Updating
h_close = {'Connection': 'Close'}
h_content = {'Content-Type': 'application/json'}
car = {'id': 6,
       'brand': 'Mercedes Benz',
       'model': '300SL',
       'production_year': 1967,
       'convertible': True}
try:
    reply = requests.put(
        'http://localhost:3000/cars/6', 
        headers=h_content, 
        data=json.dumps(car)
    )
    print("res=" + str(reply.status_code))
    reply = requests.get(
        'http://localhost:3000/cars/', 
        headers=h_close
    )
except requests.RequestException:
    print('Communication error')
else:
    print('Connection=' + reply.headers['Connection'])
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print('Server error')