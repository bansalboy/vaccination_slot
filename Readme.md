This Script will tell you about the Availability of Vaccination Slots with capacity. But you need to book the slot only from government authorised application or website.

**Installtion Steps**
1. Copy the script to local(on Computer) where python is installed.
2. Install the library using pip(or any other method) for pip use command pip install -r requirements.txt

**Execution of Main Script**

    python cowin.py

Run the above command on Command line(Terminal). Enter the details (PINCODE and Date ) after the execution. Script will check the slots available for next seven days(from date mentioned by you). 

**How to Read Result ?**


1. If Slots are available then result will be like this:

```
Available on 06-05-2021 with minimum age limit of 45 at SC SATIPURA capacity available : 100
Available Slots are : ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-06:00PM']
Location : SC SATIPURA Hanumangarh Junction Urban Primary Health Center
```
Please Read Date and Minimum Age carefully.

2. If Slots are not available then it will show message like

```
Sorry No Availabilities as of now. Please try again in an hour
```
