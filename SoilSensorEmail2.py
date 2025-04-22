# import the time module

import time

# get the current time in seconds since the epoch

seconds = time.time()

print("Seconds since epoch =", seconds)

result = time.localtime(seconds)

print("Current TIME Hour:", result.tm_hour + 8)

# Set the LastValue variable. Will compare to Current Hour Value

# lastValue = result.tm_hour + 8

startTime = 19

lastValue = startTime

print ("Time to send the FIRST email of the day")

while (True):

 result = time.localtime(seconds)

 Current_Value = result.tm_hour + 8

 # Compare Time to send email

if (lastValue == Current_Value):

    print ("IGNORE")

else:

 difference = Current_Value - lastValue

if (difference > 3):

 print ("Time difference > 3. Time to send an email")

lastValue = Current_Value

else:

 print ("Hour Difference < 4. Do NOT Email")
