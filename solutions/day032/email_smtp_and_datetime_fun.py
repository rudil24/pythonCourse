# rudil24
# Day 32: smtp and datetime functions
# documenting the code but not enacting it with any real email addresses.
# smtp information:
# gmail is smtp.gmail.com
# yahoo is smtp.mail.yahoo.com
# hotmail is smtp.live.com
# outlook is smtp-mail.outlook.com
#
# when you do msg="Subject: <your_subject>\n\n <your body>" it will do subject and body correctly on the other end
# you can also f string it to put {variables} in the subject and/or body


import smtplib
import datetime as dt

my_email = "XZ2yS@example.com"
password = "password"  # to get the real one, go to "manage account"; "security" tab; turn on 2-step verification, then go to "App Passwords"; generate for "Other", name this app, get the password.

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
current_date = f"{day}/{month}/{year}"
date_of_birth = dt.datetime(year=1999, month=12, day=31, hour=4, minute=30)
current_time = now.hour
weekday = now.weekday()
if (
    weekday == 0
):  # 0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday, 5 = Saturday, 6 = Sunday
    with smtplib.SMTP(
        "smtp.gmail.com"  # or smtp.mail.yahoo.com or smtp.live.com (hotmail) or smtp-mail.outlook.com, depending on provider
    ) as connection:  # the other way to do it instead of with/as: connection = smtplib.SMTP("smtp.gmail.com") but then you have to remember to connection.close() at the end of your block
        connection.starttls()  # tls = transport layer security: secure the connection (encrypt)
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="bDZ2j@example.com",
            msg="Subject: Monday Motivation\n\n" "Work hard, play hard",
        )
