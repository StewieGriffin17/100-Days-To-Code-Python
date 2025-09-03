import random
import smtplib
import datetime as dt

my_email = "your_email@gmail.com"
password = "your_email_app_password"  # you can get this from the security tab inside google account.

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: Monday Motivation\n\n{quote}"
        )
