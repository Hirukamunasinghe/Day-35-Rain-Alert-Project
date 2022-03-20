import requests
from twilio.rest import Client

api_key ="8b25d09b37ba5597bf54d9aa3f25988d"
OWM_endpoint ="https://api.openweathermap.org/data/2.5/onecall"
account_sid ="AC9feb75250fc87b0b51477f05649a9bcd"
auth_token ="0dcafb3b91c9019e7d2d84b5a13da1e8"

weather_params ={
    "lat":6.864908,
    "lon":79.899681,
    "appid":api_key,
    "exclude":"current,minutely,daily"
}

response = requests.get(OWM_endpoint,params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) <700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Its going to rain today. Pls bring an umbrella☂️",
        from_='+15625241336',
        to='+94762193001'
    )

    print(message.status)