import requests
from twilio.rest import Client

parameters = {
    "lat": 23.7104,
    "lon": 90.4074,
    "appid": "Your_own_api_key",  # You can get this by creating an account in the openweather website.
    "cnt": 4,
}

# You can get those from twilio dashboard.
account_sid = "your account sid"
auth_token = "your auth token"

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

data = response.json()

will_rain = False
for hour_data in data["list"]:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from="your number from twilio",
        to="your verified number",
    )
    print(message.status)
