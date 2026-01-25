# rudil24
# Day 38: Workout Tracker

APP_ID = "app_6231b44b78fb4407930108ba"
API_KEY = "nix_live_e84MpEis5O8Fj0R9V1pJ69LuDJG3j2bp"

# Use these credentials in your API requests by including them as headers:

# x-app-id: app_6231b44b78fb4407930108ba
# x-app-key: nix_live_e84MpEis5O8Fj0R9V1pJ69LuDJG3j2bp

import requests

GENDER = "male"
WEIGHT_KG = 90.9  # 210 lbs in kg is 90.9
HEIGHT_CM = 175  # 5'10'' in cm is 175
AGE = 56

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)
