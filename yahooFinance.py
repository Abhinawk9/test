import csv
from urllib.request import urlopen
from yahoo_finance import Share
from bs4 import BeautifulSoup
page_id = 'https://finance.yahoo.com/quote/'
quote_page_500SP = ['MMM','ABT','ABBV','ACN','ATVI','AYI','ADBE','AMD','AAP','AES','AET','AMG','AFL','A','APD','AKAM','ALK','ALB','ARE'
                    'ALXN','ALLE','AGN','ADS','LNT','ALL','GOOGL','GOOG','MO','AMZN','AEE','AAL','AEP','AXP','AIG','AMT','AWK','AMP','ABC',
                    'AME','AMGN','APH','APC','ADI','ANDV','ANSS','ANTM','AON','AOS','APA','AIV','AAPL','AMAT','ADM','ARNC','AJG','AIZ','T']
                    
for pg in quote_page_500SP:
    pg1= pg
    yahoo = Share(pg)
    pg = page_id+pg+'/key-statistics?p='+pg
    page = urlopen(pg)
    soup = BeautifulSoup(page, "html.parser")
    statics_box = soup.find("td", attrs={"data-reactid": "26"})
    statics = statics_box.text.strip()
    with open("quote1.csv","a") as csv_file:
        writer=csv.writer(csv_file)
        writer.writerow([pg1,yahoo.get_price(),yahoo.get_trade_datetime(),statics])
print('COMPLETED')
    
