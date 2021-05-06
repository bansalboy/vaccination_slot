import requests
import json
import sys


PINCODE = input("Enter the PINCODE of your Location : ")
try:
    DATE = raw_input(
        "Enter the date in this format DD-MM-YYYY ex: 05-05-2021 : ")
except Exception as e:
    DATE = input("Enter the date in this format DD-MM-YYYY ex: 25-05-2021 : ")


# PINCODE = "335512"
# DATE = "06-05-2021"
url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(
    PINCODE, DATE)
# print url
headers = {'accept': 'application/json, text/plain, */*',
           'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
           'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'}

response = requests.get(url=url, headers=headers).json()
# print response
found = False
try:
    for center in response["centers"]:
        for session in center["sessions"]:
            # print session
            if session["available_capacity"] > 0:
                print("Available on {} with minimun age limit of {} at {} capacity available : {} ".format(
                    session["date"], session["min_age_limit"], center["name"], session["available_capacity"]))
                print("Location : {}".format(center["address"]))
                found = True
    if not found:
        print("Sorry No Availabilities as of now. Please try again in an hour")
except Exception as e:
    print("Error!")
    print(e)
