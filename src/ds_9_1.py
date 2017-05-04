import requests
import json
url='http://freegeoip.net/json/'
geostr=requests.get(url).text
js = json.loads(geostr)

for key in js.keys():
    print key,
    print js[key]