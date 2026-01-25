##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
import random
import smtplib

MY_EMAIL = "YOUR_EMAIL"
MY_PASSWORD = "YOUR_APP_PASSWORD"

# 1. Update the birthdays.csv
data = pd.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()

# Filter for rows where month and day match today
birthday_people = data[(data.month == today.month) & (data.day == today.day)]

# 3. If step 2 is true, pick a random letter from .\letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
for index, person in birthday_people.iterrows():
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", person["name"])

    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}",
        )
