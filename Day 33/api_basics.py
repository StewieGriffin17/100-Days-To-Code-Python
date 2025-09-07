import requests
from datetime import datetime

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)

parameters = {
    "lat": 23.810331,
    "lng": 90.412521,
    "formatted": 0
}

response2 = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response2.raise_for_status()

data2 = response2.json()
sunrise = data2["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data2["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)
