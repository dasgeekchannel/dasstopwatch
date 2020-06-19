#Stopwatch program created by DasGeek
#Fill your Brains!
#Used for managing time of segments in Destination Linux

import pyfiglet                 # import Pyfiglet module
import datetime                 # import datetime module
from time import sleep          # import sleep
from selenium import webdriver  # import selenium to insert text into Codi document
ascii_banner = pyfiglet.figlet_format("Das   Stopwatch")  # ascii banner using Pyfiglet
print(ascii_banner)
print("\n")
print('Type "S" to Start Time')
print("\n")
count = 0 # each S entered should increase count and print segment number
print(datetime.datetime.now().time())
userstart = input('Enter "s" to Start and "ss" to STOP : ' )
if userstart == "s":
    print("Segment Started")
    start = datetime.datetime.now()
    end = datetime.datetime.now()
    elapsed = end - start
    print(elapsed)
    # or
    print(elapsed.seconds, ":", elapsed.microseconds)

import datetime as dt
# Save the current time to a variable ('t')
t = dt.datetime.now()
while True:
    delta = dt.datetime.now()-t
    if delta.seconds == 60: # Get 60 second mark and print text
        print("1 Min")
        break # stop after gets to 60 seconds
while True: #move to next milestone
    delta = dt.datetime.now()-t
    if delta.seconds == 90: #change seconds here to actually be 10 min. Use 90 for testing.
        print("10 Min Warning...\n time to close your stupid hole and move on you muppet!")
        userstop = input('Type ss to stop:  ')
        if userstop == "ss":
            break
            print("Segment Stopped")

# Section in testing to post to document with warning messages executed after SS is invoked
#from selenium import webdriver

#driver = webdriver.Firefox()
#driver.get("https://")

#driver.find_element_by_id("textarea").send_keys("Selenium")

#Area to add random notes, guides, and future improvement ideas.
#https://pythonspot.com/selenium-textbox/
#Segment1 =
#Segment2 =
#Segment3 =
#Segment4 =
#Segment5 =
