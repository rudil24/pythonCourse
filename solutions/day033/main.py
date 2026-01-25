import requests
import datetime

MY_LAT = 43.610119  # Meridian, ID USA latitude
MY_LONG = -116.391571  # Meridian, ID USA longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# function to check if Your position is within +5 or -5 degrees of the ISS position.
def is_iss_overhead():
    if (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
        and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    ):
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = datetime.datetime.fromisoformat(data["results"]["sunrise"])
sunset = datetime.datetime.fromisoformat(data["results"]["sunset"])

sunrise_hour = sunrise.astimezone().hour  # .astimezone() is to convert to local time
sunset_hour = sunset.astimezone().hour

time_now = datetime.datetime.now(datetime.timezone.utc).astimezone()


def is_night():
    if time_now.hour >= sunset_hour or time_now.hour <= sunrise_hour:
        return True
    else:
        return False


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

print(
    f"Your position: {MY_LAT}, {MY_LONG}\nISS position: {iss_latitude}, {iss_longitude}"
)
print(f"Sunrise: {sunrise_hour}, Sunset: {sunset_hour}, Current Hour: {time_now.hour}")
print(f"Is ISS overhead? {is_iss_overhead()}\nIs it night? {is_night()}\n")
if is_iss_overhead() and is_night():
    print("Look up!")  # just doing a print statement for now, will wire up email later
    # BONUS: run the code every 60 seconds.
    # import time
    # while True:
    #     time.sleep(60)
    #     if is_iss_overhead() and is_night():
    #         print("Look up!")
    #     else:
    #         print("Look down!")
    #         break
