from datetime import datetime, timedelta

right_now = datetime.now()

right_now = timedelta( hours = right_now.hour, minutes = right_now.minute)   


new_time = timedelta(hours = 22, minutes = 30)

if right_now < new_time:
    print "cool"
    print right_now, "<", new_time
    
else:
    print "not cool"
    print right_now, ">", new_time


