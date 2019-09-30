import requests
import time
import turtle
import os

astronaut_data = 'http://api.open-notify.org/astros.json?api_key=' + os.environ.get('KEY')

result = requests.get(astronaut_data).json()

print('People in Space {}'.format(result['number']))

for person in result['people']:
    print(person['name'] + ' in ' + person['craft'])


iss_location = 'http://api.open-notify.org/iss-now.json?api_key=' + os.environ.get('KEY')

while True:

    coordinates = requests.get(iss_location).json()
    timestamp = coordinates['timestamp']
    lat = coordinates['iss_position']['latitude']
    lon = coordinates['iss_position']['longitude']
    print('Time: ' + str(timestamp) + ' ' + 'Latitude: {}  Longitude: {}'.format(lat, lon))

    screen = turtle.Screen()
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -190, 180, 90)
    screen.bgpic('images/NASA_World_Map.gif')
    screen.register_shape('images/ISS.gif')
    iss = turtle.Turtle(visible=False)
    iss.shape('images/ISS.gif')
    iss.penup()
    iss.goto(float(lon), float(lat))
    iss.showturtle()

    time.sleep(.1)
