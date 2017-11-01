import requests
from lxml import html
pageContent = requests.get('https://finance.yahoo.com/quote/MMM/')
tree=html.fromstring(pageContent.content)
price=tree.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]/text()')
print (price)
