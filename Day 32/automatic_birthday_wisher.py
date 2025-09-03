import random
import smtplib
from datetime import datetime
import pandas

my_email = "your_email@gmail.com"
password = "your_email_app_password"

"""
To get app password for your gmail ->
1. go to google account setting
2. open the security tab
3. choose the app password option
4. generate a new app password for this program
5. paste it here without any space
6. now you are good to go
"""

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{contents}"
        )
        connection.close()
