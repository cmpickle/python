import urllib
import urllib2
import webbrowser
import datetime
from datetime import date
from apscheduler.scheduler import Scheduler
 
#sched = Scheduler()
#sched.start()
 
confNum = "B99KQH"
fName = "Cameron"
lName = "Pickle"
data = {
    "confirmationNumber" : confNum,
    "firstName" : fName,
    "lastName" : lName
    }
 
encoded_data = urllib.urlencode(data)
content = urllib2.urlopen("https://www.southwest.com/flight/retrieveCheckinDoc.html", encoded_data)
with open("results.html", "w") as f:
    f.write(content.read())
webbrowser.open("results.html")
 
#def confirm():
#    return
 
#exec_date = date(2017, 1, 26)
 
#job = sched.add_date_job(confirm, exec_date)
 
#job = sched.add_date_job(confirm, datetime(2017, 1, 26, 15, 22, 0))