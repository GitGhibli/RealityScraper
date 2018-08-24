from geopy.geocoders import Bing
import json
import time
import math

class JsonEncoder(json.JSONEncoder):
    def default(self, z): # pylint: disable=E0202
        return z.__dict__

with open(r'Output\data.txt') as f:
    data = json.load(f)

geolocator = Bing('ApfjtgVg2-JtMzi3b-sdJYnHNE6bpkRIdug30idpvaB-cF51TsA_BnppDBXRSujo', timeout=None)

totalData = len(data)
counter = 0

for dataItem in data:
    counter = counter + 1
    print(str(counter)+"["+str(math.floor((counter/totalData)*100))+'%]'+dataItem['address'])
    loc = geolocator.geocode(dataItem['address']+' '+dataItem['area']+' New Zealand')
    dataItem['latitude'] = loc.latitude
    dataItem['longitude'] = loc.longitude

with open(r'Output\GeoCoder\out' + str(time.time()) + ".txt", "w") as f:
    f.write(json.dumps(data, cls=JsonEncoder))