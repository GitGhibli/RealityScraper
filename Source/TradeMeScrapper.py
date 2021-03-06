import requests
from scrapy.selector import Selector
import time
import re
import json

tradeMeUrl = "https://www.trademe.co.nz/property/residential-property-to-rent/auckland"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

nextLink = ""
data = []

class DataItem:
    def __init__(self, link, address, area, price, repeat):
        self.link = link
        self.address = address
        self.area = area
        self.price = price
        self.repeat = repeat

class JsonEncoder(json.JSONEncoder):
    def default(self, z): # pylint: disable=E0202
        return z.__dict__

def processPage(url, data, depth):
    startDataCount = len(data)
    print("Processing: " + url)
    response = requests.get(url, headers=headers)
    # results = Selector(response=response).xpath('//ul[@class="list-view-list"]/li[not(@style="display: none;")]') #not() does not work in scrapy
    results = Selector(response=response).xpath('//ul[@class="list-view-list"]/li')
    nextLink = Selector(response=response).xpath('//a[@rel="next"]/attribute::href').extract_first()

    for result in results:
        linkWithToken = result.xpath('./a/attribute::href').extract_first()
        address = result.xpath('.//div[contains(@class,"tmp-search-card-list-view__title")]/text()').extract_first()
        area = result.xpath('.//div[contains(@class,"tmp-search-card-list-view__subtitle")]/text()').extract_first()
        priceRaw = result.xpath('.//div[contains(@class,"tmp-search-card-list-view__price")]/text()').extract_first()

        if linkWithToken is None or priceRaw is None:
            continue
        
        link = re.search(r'(.*)\?', linkWithToken)[1]
        price = re.search(r'\$([,\d]+)([ \w]+)', priceRaw)

        data.append(DataItem(link, address, area, price[1], price[2].strip()))
    
    endDataCount = len(data)
    print("Realities found:" + str(endDataCount))

    if nextLink is not None and startDataCount != endDataCount and depth < 2:
        processPage("https://www.trademe.co.nz/" + nextLink, data, depth + 1)

processPage(tradeMeUrl, data, 0)

f = open(r'Output\tradeMeOutput' + str(time.time()) + ".txt", "w")
f.write(json.dumps(data, cls=JsonEncoder))
f.close()