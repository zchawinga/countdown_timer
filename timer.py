#! How much time do I have to submit my SIGCSE paper?
# Ack: isidore.john.r at gmail dot com
from time import time, gmtime, mktime, strftime #Add time stuff
from datetime import datetime, timedelta #Add timedelta
deploy = datetime(2017, 9, 2, 16, 59) #Based on local-time PDT -7GMT, AOE -12GMT
timestamp = time.mktime(deploy.timetuple())
deploy_utc = datetime.utcfromtimestamp(timestamp)
elapsed = deploy_utc - datetime.utcnow() # `deploy` is in the future
trunc_micros = timedelta(days=elapsed.days, seconds=elapsed.seconds) # remove microseconds
print("SIGCSE Deadline")
print(trunc_micros) 
#CC NC-AT chawingaconsulting @ccg_usa
