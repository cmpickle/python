import requests
import smtplib
from smtplib import SMTP

main_api = 'https://www.utahrealestate.com/search/chained.update/count/false/criteria/false/pg/1/limit/50/dh/831/using_map_viewport/true?param=geometry&value=POLYGON%28%28-112.02518463134624%2040.39715650342232%2C-111.9067382812428%2040.39715650342232%2C-111.9067382812428%2040.61408275138994%2C-112.02518463134624%2040.61408275138994%2C-112.02518463134624%2040.39715650342232%29%29&param_reset=county_code,o_county_code,city,o_city,zip,o_zip,geometry,o_geometry&chain=saveLocation,criteriaAndCountAction,mapInlineResultsAction&all=1&accuracy&geocoded&state&box&htype&lat&lng&selected_listno&type=1&geolocation&listprice1&listprice2=320000&tot_bed1=3&tot_bath1=2&stat=1&env_certification&o_env_certification=32&status=1&proptype=1&style&o_style=4&tot_sqf1=2000&dim_acres1&yearblt1&cap_garage1=2&opens&accessibility&o_accessibility=32&loc&accr&op=16777216&advanced_search=0&param_reset=housenum,dir_pre,street,streettype,dir_post,city,county_code,zip,area,subdivision,quadrant,unitnbr1,unitnbr2,geometry,coord_ns1,coord_ns2,coord_ew1,coord_ew2,housenum,o_dir_pre,o_street,o_streettype,o_dir_post,o_city,o_county_code,o_zip,o_area,o_subdivision,o_quadrant,o_unitnbr1,o_unitnbr2,o_geometry,o_coord_ns1,o_coord_ns2,o_coord_ew1,o_coord_ew2'
url = main_api

json_data = requests.get(url).json()

json_listing_data = json_data['listing_data']
markers = json_data['markers']
# for i in range(0, len(json_listing_data)):
#	print("https://www.utahrealestate.com/" + json_data['listing_data'][i]['listno'])



txtdoc = '.\house_check.txt'
file = open(txtdoc, 'w+')
print "I'mma scrape you good!"

listing = []
for i in range(len(markers)):
                listing.append("%s %s %s" % (markers[i]['id'], markers[i]['price'], 'https://utahrealestate.com/' + markers[i]['id']))
file.close()
 
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('autom8edpickle@gmail.com', 'Pickle42')
 
# print listing
write = False
for house in listing:
                file = open(txtdoc, "r+")
                with open(txtdoc, "a+") as file:
                                for lines in file.read().split("\n"):
                                                if house == lines:
                                                                write = False
                                                                break
                                                else:
                                                                write = True
                                if write:
                                                file.seek(0,2)
                                                file.write("\n" + house)
                                                smtpObj.sendmail('autom8edpickle@gmail.com', '8016948594@tmomail.net', 'Subject: House \n%s' % house)
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
