import os
import datetime
import requests
import time
import turtle
import webbrowser

# initialize api with astronaut data
astronaut_data = 'http://api.open-notify.org/astros.json?api_key=' + os.environ.get('KEY')
# format api data to json
result = requests.get(astronaut_data).json()
# print number of people in space
print('People in Space {}'.format(result['number']))
# print name and craft of each person in space
for person in result['people']:
    print(person['name'] + ' in ' + person['craft'])

# initialize api with iss data
iss_location = 'http://api.open-notify.org/iss-now.json?api_key=' + os.environ.get('KEY')

while True:
    # format api iss data to json
    coordinates = requests.get(iss_location).json()
    # store timestamp, latitude, and longitude in variables
    timestamp = coordinates['timestamp']
    lat = coordinates['iss_position']['latitude']
    lon = coordinates['iss_position']['longitude']
    # print formatted timestamp and lat,lon coordinates to console
    print('Time: ' + str(datetime.datetime.fromtimestamp(timestamp)) + ' ' + 'Latitude: {}  Longitude: {}'.format(lat, lon))
    # initialize iss icon and map to display iss location on map
    screen = turtle.Screen()
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -190, 180, 90)
    # set map image
    screen.bgpic('images/NASA_World_Map.gif')
    # set iss icon on map
    screen.register_shape('images/ISS.gif')
    # initialize turtle and turn off visibility of original turtle icon
    iss = turtle.Turtle(visible=False)
    # set turtle icon to desired image
    iss.shape('images/ISS.gif')
    iss.penup()
    iss.goto(float(lon), float(lat))
    iss.showturtle()

    time.sleep(.1)
    # create variable to google maps url with lat,lon coordinates
    google_maps = f"http://maps.google.com/?q={lat},{lon}"
    # open google maps tab with iss location drop point
    webbrowser.open_new_tab(google_maps)
    # keep turtle running to avoid closing display immediately
    turtle.mainloop()
