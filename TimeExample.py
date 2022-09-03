'''
Time examples

'''
# import Python Standard Time Libraries
import time
from datetime import datetime

import pytz  # Python Timezone Library

''' Determine what the time was at the epoch 
    if we request the time at the 0 offset 
    we will get the time at the epoch for this
    machine.
'''

timeAtEpoch = time.gmtime(0)  # gmtime returns the time at the desired offset
print("\nEPOCH: ", timeAtEpoch)  # it provides details regarding that date/time

''' Display a more human readable form '''
timeStr = time.asctime(timeAtEpoch)
print("Human readable: ", timeStr)

'''
What is the time now?
'''
print("\nWhat is the Time Now?")

gmtNow = time.gmtime()
localNow = time.localtime()
print("Time at Greenwich:   ", time.asctime(gmtNow))
print("Time at Local:       ", time.asctime(localNow))

''' Getting my Local Time Zone '''
now = datetime.now()
print("Local Time zone:     ", now.astimezone().tzinfo)

''' Getting time in another Time Zone '''

print("\nForeign City Times")
parisTime = pytz.timezone("Europe/Paris")
timeInParis = datetime.now(parisTime)
print("Paris:", timeInParis.strftime("%m/%d/%Y, %H:%M:%S"))

print("\nAll Locations")
print("=" * 60)
for tz in pytz.all_timezones:
    loc = pytz.timezone(tz)
    timeInLoc = datetime.now(loc)
    print('{:30s}'.format(tz), timeInLoc.strftime("%m/%d/%Y, %H:%M:%S"))
