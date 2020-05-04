"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
#create a dict to keep tel number and time key-value pairs
time = {}
for record in calls:
    if record[0] not in time:
        time[record[0]] = int(record[3])
    else:
        time[record[0]] += int(record[3])

    if record[1] not in time:
        time[record[1]] = int(record[3])
    else:
        time[record[1]] += int(record[3])


longest_phone_call = max(time,key=lambda x:time[x])
print(str(longest_phone_call) + " spent the longest time, "+ str(time[longest_phone_call])+" seconds, on the phone during September 2016")
