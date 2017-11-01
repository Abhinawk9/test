from urllib.request import urlopen
from bs4 import BeautifulSoup
quote_page = 'https://finance.yahoo.com/quote/MMM/'
#quote_page=["http://www.bloomberg.com/quote/SPX:IND", "http://www.bloomberg.com/quote/CCMP:IND"]
page = urlopen(quote_page)
soup = BeautifulSoup(page, "html.parser")
name_box = soup.find("h1", attrs={"data-reactid": "7"})
name = name_box.text.strip() 
print (name)
#price_box = soup.find("span", attrs={"class_" :"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"})
price_box = soup.find("span", attrs={"data-reactid": "35"})
price = price_box.text
print (price)
statics_page='https://finance.yahoo.com/quote/MMM/key-statistics?p=MMM'
page1 = urlopen(statics_page)
soup = BeautifulSoup(page1, "html.parser")
#import time
#time.sleep(15)
#statics_box = soup.find("td", attrs={"data-reactid": "26"})
#statics = statics_box.text.strip() 
#print (statics)
#import csv
#from datetime import datetime
#with open("index.csv", "a") as csv_file:
 #writer = csv.writer(csv_file)
 #writer.writerow([name, price,statics, datetime.now()])

