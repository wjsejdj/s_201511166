
import os
import requests
import src.mylib
import urlparse
import lxml
import lxml.etree
import StringIO

keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
key=src.mylib.getKey(keyPath)
KEY=str(key['dataseoul'])
TYPE='xml'
SERVICE='SearchSTNBySubwayLineService'
START_INDEX=str(1)
END_INDEX=str(10)
for line in range(1,10):
    LINE_NUM=str(line)
    params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX,LINE_NUM)
    _url='http://openAPI.seoul.go.kr:8088/'
    url=urlparse.urljoin(_url,params)
    url = url.replace('\\','/')
    data=requests.get(url).text
    tree = lxml.etree.fromstring(data.encode('utf-8'))
    nodes = tree.xpath('//STATION_NM')
    for node in nodes:
        print node.text