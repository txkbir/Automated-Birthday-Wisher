import os
import smtplib
import datetime as dt
import pandas

PASSWORD = os.environ['PASSWORD']
FROM = 'takbirr04@gmail.com'


now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

DataFrame = pandas.read_csv('birthdays.csv')
birthdays_dict = {(row.month, row.day): row for _, row in DataFrame.iterrows()}

if today in birthdays_dict:
    person_name = birthdays_dict[today]['name']
    TO = birthdays_dict[today]['email']
    with open('letter_templates/letter.txt') as file:
        contents = file.read()
        letter = contents.replace('[NAME]', person_name)
        if person_name == 'Ma' or person_name == 'Abbuji' or person_name == 'Grace':
            letter = letter.replace('Have a great day', 'I love you so much')

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=FROM, password=PASSWORD)
        connection.sendmail(from_addr=FROM, to_addrs=TO, msg=f'Subject:Happy Birthday {person_name}!\n\n{letter}')
