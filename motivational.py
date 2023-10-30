from random import choice
import smtplib
import datetime as dt

my_email = "gholapyash.smtplib@gmail.com"
password = "mspdzmptjgvmsoiy"

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 6:
    try:
        with open("quotes.txt") as quotes_data:
            contents = quotes_data.readlines()
    except FileNotFoundError as error:
        print(f"{error} does not exist.")
    else:
        new_content = choice(contents)
    finally:
        print(new_content)

    try:
        connection = smtplib.SMTP("smtp.gmail.com")
    except ConnectionError:
        print("Connection was not established.please check the credentials and try again.")
    else:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="gholapyash@gmail.com",
                            msg=f"subject:Motivational quotes\n\n {new_content}")
else:
    print("sorry day is not sunday")

# import smtplib
#
# my_email = "gholapyash.smtplib@gmail.com"
# password = "mspdzmptjgvmsoiy"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="gholapyash@gmail.com",
#                         msg="subject:hello\n\nThis is the body of my email"
#                         )
#
# import datetime as dt
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# day = now.day
#
# dob = dt.datetime(year=2000, month=5, day=19, hour=8)
# print(dob)
