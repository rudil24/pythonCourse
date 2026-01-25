import requests  # need to install the requests package
from datetime import datetime

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# if response.status_code == 200:
#     data = response.json()
#     longitude = data["iss_position"]["longitude"]
#     latitude = data["iss_position"]["latitude"]
#     print(longitude, latitude)
# else:
#     raise Exception(
#         f"Request failed with status code {response.status_code} and message {response.text}"
#     )

# # easier way than above, using requests own raise_for_status method
# response.raise_for_status()
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)
# # put that position into
# # https://www.latlong.net/Show-Latitude-Longitude.html
# # for a quick view of where the ISS is

# sunrise/sunset example
parameters = {
    "lat": 43.610119,
    "lng": -116.391571,
    "formatted": 0,
}  # Meridian, ID USA lat/long
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
# {'results': {'sunrise': '2026-01-19T15:11:32+00:00', 'sunset': '2026-01-20T00:41:12+00:00', 'solar_noon': '2026-01-19T19:56:22+00:00', 'day_length': 34180, 'civil_twilight_begin': '2026-01-19T14:41:44+00:00', 'civil_twilight_end': '2026-01-20T01:11:00+00:00', 'nautical_twilight_begin': '2026-01-19T14:06:35+00:00', 'nautical_twilight_end': '2026-01-20T01:46:10+00:00', 'astronomical_twilight_begin': '2026-01-19T13:32:26+00:00', 'astronomical_twilight_end': '2026-01-20T02:20:19+00:00'}, 'status': 'OK', 'tzid': 'UTC'}
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise)
print(sunset)
