from lxml import html
import requests
import smtplib
from smtplib import SMTP

# Create a text document to keep track of already seen listings
txtdoc = 'C:\Users\%USERNAME%\Documents\ksl_check.txt'
file = open(txtdoc, 'w+')

print "I'mma scrape you good!"

# input the search url below
page = requests.get('http://www.ksl.com/auto/search/index?keyword=&yearFrom=1996&yearTo=&mileageFrom=1000&mileageTo=90000&priceFrom=&priceTo=5000&zip=&miles=0&newUsed%5B%5D=All&page=0&sellerType=&postedTime=&titleType=Clean+Title&body=&transmission=&cylinders=&liters=&fuel=&drive=&numberDoors=&exteriorCondition=&interiorCondition=&cx_navSource=hp_search&search.x=67&search.y=11&search=Search+raquo%3B')

# Specify the information to scrape from KSL
tree = html.fromstring(page.content)
titles = tree.cssselect("h2.title a.link")
price = tree.cssselect("div.listing-detail-line.price")
miles = tree.cssselect("div.listing-detail-line.mileage")
urls = tree.xpath('/html/body/div/div/div/div/main/div/div/div/h2//a/@href')

# Format the scraped information into a listing array
listing = []
for i in range(len(price)):
                listing.append("%s %s %s" % (titles[i].text_content().strip(), price[i].text_content().strip(), miles[i].text_content().strip()))
file.close()
 
# Setup the smtp object  
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()

# This python script uses a pii.txt that cotains the following three values separated by a newline:
# emailAddress (The email that you have opened for stmp access)
# password (the email's login password)
# destinationAddress (This could be another email or can be set to a phone number for email to sms ie: 8015555555@tmomail.net)
pii = open('pii.txt', 'r+')
username = pii.readline()
password = pii.readline()
phoneAddress = pii.readline()
pii.close()

# Login to the smtp account
smtpObj.login(username, password)

# Send the listing from the smtp email account to the desination address
write = False
for car in listing:
    with open(txtdoc, "a+") as file:
        for lines in file.read().split("\n"):
            if car == lines:
                write = False
                break
            else:
                write = True
        if write:
            file.seek(0, 2)
            file.write("\n" + car)
            smtpObj.sendmail(username, phoneAddress,
                             'Subject: Cars \n%s' % car + 'http://ksl.com' + urls[listing.index(car)])
            write = False
    file.close()
smtpObj.quit()
file.close()

# read the check file and if there are more than {max} records clear them out
# this is to make sure the file doesn't get overly large
max = 60
with open(txtdoc, 'r') as fin:
    data = fin.read().splitlines(True)
begin = data.__len__() - max - 1
if begin < 0:
    begin = 0
with open(txtdoc, 'w') as fout:
    fout.writelines(data[begin:])
