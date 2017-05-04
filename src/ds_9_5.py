import os
import requests
import mylib
import lxml
import lxml.etree
srcPath = os.path.join(os.getcwd(),'src','key.properties')
key = mylib.getKey(srcPath)
_url='http://openAPI.seoul.go.kr:8088'
_key=str(key['dataseoul'])
_type='xml'
_service='CardSubwayStatisticsService'
_start_index=1
_end_index=5
_use_mon='201306'
_api=os.path.join(_url,_key,_type,_service,str(_start_index),str(_end_index),_use_mon)
_api = _api.replace('\\','/')
request = requests.get(_api).text

tree = lxml.etree.fromstring(request.encode('utf-8'))
nodes = tree.xpath('//row')
for node in nodes:
    LINENUM = node.xpath('./LINE_NUM')
    print LINENUM[0].text,
    SUBSTAIONNM = node.xpath('./SUB_STA_NM')
    print SUBSTAIONNM[0].text,
    RIDE_PASGR_NUM = node.xpath('./RIDE_PASGR_NUM')
    print RIDE_PASGR_NUM[0].text,
    ALIGHT_PASGR_NUM = node.xpath('./ALIGHT_PASGR_NUM')
    print ALIGHT_PASGR_NUM[0].text