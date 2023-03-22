import os, sys
from collections import defaultdict

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

##collect all input, or "timestamps"
with open(os.path.join(dirname, "input.txt")) as timestamp_list:
    timestamps = [timestamps.split() for timestamps in timestamp_list]

##sort list by time
timestamps = sorted(timestamps)

##create dictionary for schedules and initialize counter i to 0 for use in loop
schedules = {}
i = 0

##loop through timestamps to collect guard data. I'm using a 
##while loop because iteration is weird and this makes sense to me:
##each loop should be one guard's "block" in the schedule
while i < len(timestamps):
    timestamp = timestamps[i]
    ##initializing counter j, which helps us keep track of where we
    ##are in the current guard's "block"
    j = 1

    ##we'll always want to be able to see one timestamp ahead
    next_timestamp = timestamps[i + j]

    ##since each loop is one guard's "block", this should always
    ##be the guard's ID
    guard = timestamp[3]
    
    ##if this is the first time we've seen this guard, initialize
    ##his schedule
    if guard not in schedules:
        schedules[guard] = defaultdict(int)

    guards_schedule = schedules[guard]

    ##loop until we get to the next guard's "block"
    while next_timestamp[2] != "Guard":

        ##we should always be at a "falls asleep" section here
        if next_timestamp[2] == "falls":

            ##get minute timestamp of when the guard falls asleep
            ##REMEMBER guards only fall asleep in midnight hour, so
            ##we only have to check the minutes
            fall_timestamp = int(next_timestamp[1].split(":")[1][:-1])

            ##once the guard falls asleep, we look to the next line to 
            ##see when he wakes up and store that minute too
            j += 1
            next_timestamp = timestamps[i + j]
            wake_timestamp = int(next_timestamp[1].split(":")[1][:-1])

            ##loop through the minutes he's asleep
            for k in range(fall_timestamp, wake_timestamp):

                ##if the guard has been asleep in this minute before,
                ##we increment the counter
                if k in guards_schedule:
                    guards_schedule[k] += 1
                ##otherwise we initialize the counter
                else:
                    guards_schedule[k] = 1
        
        ##now set the counter to look to the next line
        j += 1

        ##if we haven't run out of timestamps, set next_timestamp
        if (i + j) < len(timestamps):
            next_timestamp = timestamps[i + j]
        ##otherwise break
        else:
            break
    
    ##loop ahead to the next guard's "block"
    i += j

#create a dictionary of integers to keep track of each guard's minutes asleep
sleepy_minutes = defaultdict(int)

#loop through each guard to tally their minutes asleep and store it in the dict
for key, schedule in schedules.iteritems():
    sum = 0
    for minute in schedule:
        sum += schedule[minute]

    sleepy_minutes[key] = sum

##find the guard with the most minutes asleep
sleepiest_guard = max(sleepy_minutes, key=lambda k: sleepy_minutes[k])

##then find his minute most often asleep
sleepiest_minute = max(schedules[sleepiest_guard], key=lambda k: schedules[sleepiest_guard][k])

##and get their product
product = int(sleepiest_guard[1:]) * sleepiest_minute

print(product)