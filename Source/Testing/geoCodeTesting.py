from geopy.geocoders import Bing

addresses = [
    ('Fully,Furnished,MILFORD,MARINA	Milford', 'North,Shore,City'),
    ('unit/18,Centreway,Road	Orewa', 'Rodney'),
    ('Whitford	Whitford', 'Manukau,City'),
    ('Lonely,Track,road	Albany', 'North,Shore,City'),
    ('1102/30,Beach,Road	City,Centre', 'Auckland,City'),
    ('Otara	Otara', 'Manukau,City'),
    ('16,Burton,Street	Grafton', 'Auckland,City'),
    ('304/184,Symonds,Street	City,Centre', 'Auckland,City'),
    ('30/145,Quay,Street	City,Centre', 'Auckland,City'),
    ('Maplesden	Clendon,Park', 'Manukau,City'),
    ('152,Hobson,Street	City,Centre', 'Auckland,City'),
    ('732,Massey,Road	Mangere', 'Manukau,City'),
    ('Woodward	Mount,Albert', ' Auckland,City'),
    ('1,courthouse,lane', 'City,Centre, Auckland,City'),
    ('507/2,Dockside,Lane', 'City,Centre, Auckland,City')
]

# key = 'ApfjtgVg2-JtMzi3b-sdJYnHNE6bpkRIdug30idpvaB-cF51TsA_BnppDBXRSujo'
key = ""
geolocator = Bing(key)

f = open(r'Output\addCoordinates.txt', "w")

loc = geolocator.geocode('10D/8 Scotia place, Auckland City , New Zealand')
f.write('10D/8 Scotia place, Auckland City , New Zealand;' + str(loc.latitude) + ";" + str(loc.longitude) + "\n")
print(loc.latitude, loc.longitude)

for add in addresses:
    loc = geolocator.geocode(add[0] + ' ' + add[1] + ' New Zealand')
    f.write(add[0] + ' ' + add[1] + ' New Zealand;' + str(loc.latitude) + ";" + str(loc.longitude) + "\n")
    print(loc.latitude, loc.longitude)

f.close()