from lxml import html
import requests
import smtplib
from smtplib import SMTP
txtdoc = 'C:\Users\cmpic_000\Documents\check.txt'
file = open(txtdoc, 'w+')
# print "hello world"
print "I'mma scrape you good!"
page = requests.get('http://www.ksl.com/auto/search/index?keyword=&yearFrom=1996&yearTo=&mileageFrom=1000&mileageTo=90000&priceFrom=&priceTo=5000&zip=&miles=0&newUsed%5B%5D=All&page=0&sellerType=&postedTime=&titleType=Clean+Title&body=&transmission=&cylinders=&liters=&fuel=&drive=&numberDoors=&exteriorCondition=&interiorCondition=&cx_navSource=hp_search&search.x=67&search.y=11&search=Search+raquo%3B')
tree = html.fromstring(page.content)
titles = tree.cssselect("h2.title a.link")
price = tree.cssselect("div.listing-detail-line.price")
miles = tree.cssselect("div.listing-detail-line.mileage")
urls = tree.xpath('/html/body/div/div/div/div/main/div/div/div/h2//a/@href')
listing = []
for i in range(len(price)):
                listing.append("%s %s %s" % (titles[i].text_content().strip(), price[i].text_content().strip(), miles[i].text_content().strip()))
file.close()
 
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('***REMOVED***', '***REMOVED***')
 
# print listing
write = False
for car in listing:
                file = open(txtdoc, "r+")
                # file.seek(0,2)
                # print car
                with open(txtdoc, "a+") as file:
                                for lines in file.read().split("\n"):
                                                # print lines + " vs " + car
                                                if car == lines:
                                                                write = False
                                                                break
                                                else:
                                                                write = True
                                if write:
                                                file.seek(0,2)
                                                file.write("\n" + car)
                                                smtpObj.sendmail('***REMOVED***', '***REMOVED***', 'Subject: Cars \n%s' % car + 'http://ksl.com' +urls[listing.index(car)])
                                                write = False
                file.close()
smtpObj.quit()
file.close()
with open(txtdoc, 'r') as fin:
    data = fin.read().splitlines(True)
begin = data.__len__() - 30 - 1
if begin < 0:
    begin = 0
with open(txtdoc, 'w') as fout:
    fout.writelines(data[begin:])
