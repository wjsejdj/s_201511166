import os
import mylib
import requests
import json
srcPath = os.path.join(os.getcwd(),'src','key.properties')
key = mylib.getKey(srcPath)
_url='http://openAPI.seoul.go.kr:8088'
_key=str(key['dataseoul'])
_type='json'
_service='CardSubwayStatisticsService'
_start_index=1
_end_index=5
_use_mon='201306'

_maxIter=2
_iter=0
while _iter<_maxIter:
    _api=os.path.join(_url,_key,_type,_service,str(_start_index),str(_end_index),_use_mon)
    _api = _api.replace('\\','/')
    #print _api
    response = requests.get(_api).text
    js = json.loads(response)
    for item in js[_service]['row']:
        for i in item.keys():
            print item[i],
        print 
    _start_index+=5
    _end_index+=5
    _iter+=1
    