
with open("quotes.txt") as file:
    quotes = file.readlines()
    print(quotes[0])









# from smtplib import SMTP
#
# my_email = "kakashiat15@gmail.com"  # My email account
# password = "dfdsfkf"
#
# with SMTP("smtp.gmail.com") as connection: # My Email provider
#     connection.starttls()  # (tls)=Transport layer security-act as an Encryption
#     connection.login(user=my_email, password=password)  # Email and Password of mine
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="s.abhishek1715@gmail.com",
#         msg="Subject:Hello\n\nThis is body of my Email."
#     )  # To Send Email double \n To differentiate subject and body of email


import datetime as dt
# Now gives present date and time
# now = dt.datetime.now()
# year = now.year
# print(year)
# print(now.astimezone())
# print(now.date())
# print(now.second)

# me = dt.datetime(year=2003, month=11, day=15, hour=11, minute=22)  # can set or cannot HMS but compulsory YMD
# print(me)
