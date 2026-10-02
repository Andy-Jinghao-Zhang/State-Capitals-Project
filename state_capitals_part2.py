import json
import time
from geopy.geocoders import Nominatim

with open("state_capitals.json", "r") as json_file:
    capitals = json.load(json_file)

geolocator = Nominatim(user_agent="state_capitals_project")

special_addresses = {
    "Maine": "Maine State House, Augusta, Maine",
    "Massachusetts": "Massachusetts State House, Boston, Massachusetts",
    "New Hampshire": "New Hampshire State House, Concord, New Hampshire",
    "New Jersey": "New Jersey State House, Trenton, New Jersey",
    "North Dakota": "North Dakota State Capitol, Bismarck, ND",
    "Ohio": "Ohio Statehouse, Columbus, Ohio",
    "Rhode Island": "Rhode Island State House, Providence, Rhode Island",
    "South Carolina": "South Carolina State House, Columbia, South Carolina"
}

for capital in capitals:
    address = special_addresses.get(
        capital["state"],
        capital["address"]
    )

    location = geolocator.geocode(address)

    if location:
        capital["latitude"] = location.latitude
        capital["longitude"] = location.longitude
        print(capital["state"], location.latitude, location.longitude)
    else:
        capital["latitude"] = None
        capital["longitude"] = None
        print(capital["state"], "Location not found")

    time.sleep(1)

with open("state_capitals_coordinates.json", "w") as output_file:
    json.dump(capitals, output_file, indent=4)

print("state_capitals_coordinates.json created successfully.")