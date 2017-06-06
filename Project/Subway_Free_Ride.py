#-*- coding: utf-8 -*-
import sys
import matplotlib
import matplotlib.pyplot as plt
import requests
import mylib
import os
import urlparse
import lxml
import lxml.etree
import StringIO
from pymongo import MongoClient
from datetime import datetime

def PrintPersonGraph(StationName):
    for Station in d:
        if repr(Station['SUB_STA_NM']) == StationName:
            keys=[]
            values=[]
            for year in range(2015,datetime.today().year):
                for i in range(1,13):
                    key = str.format('%d%02d') % (year,i)
                    if key in Station.keys():
                        keys.append(str.format('%d%02d') % (year,i))
            for i in range(1,datetime.today().month):
                key = str.format('%d%02d') % (datetime.today().year,i)
                if key in Station.keys():
                    keys.append(str.format('%d%02d') % (datetime.today().year,i))
            for key in keys:
                values.append(Station[key])
            matplotlib.rc('font', family='HYGothic-Medium')
            matplotlib.rc('axes', unicode_minus=False)
            fig = plt.figure()
            plt.title(Station['SUB_STA_NM'] + Station['LINE_NUM'])
            plt.bar(range(len(values)),values)
            plt.xticks(range(len(keys)),keys)

    plt.show()
    
def GetData():
    todayyear = datetime.today().year
    todaymon = datetime.today().month
    _key = mylib.getKey(os.path.join('key.properties'))
    _type='xml' 
    _service= 'CardSubwayPayFree'
    _start = str(1)
    _end = str(302)
    for year in range(2015,todayyear):
        for mon in range(1,13):
            _mon = str.format("%d%02d") %(year,mon)
            url = os.path.join('http://openapi.seoul.go.kr:8088/',_key['dataseoul'],_type,_service,_start,_end,_mon)
            url = url.replace('\\','/')
            response = requests.get(url).text
            tree = lxml.etree.fromstring(response.encode('utf-8'))
            nodes = tree.xpath('//row')
            cnt=0;
            for node in nodes:
                NM = node.xpath('.//SUB_STA_NM')[0].text
                LINE = node.xpath('.//LINE_NUM')[0].text
                for cnt,Station in enumerate(d):
                    tNM = Station['SUB_STA_NM']
                    tLINE = Station['LINE_NUM']
                    if NM == tNM and tLINE == LINE:
                        cnt=-1                        
                        Station[_mon] = int(node.xpath('.//FREE_RIDE_NUM')[0].text) + int(node.xpath('.//FREE_ALIGHT_NUM')[0].text)
                        break;
                if cnt!=-1:
                    d.append(dict())
                    d[len(d)-1]['SUB_STA_NM'] = NM
                    d[len(d)-1]['LINE_NUM'] = LINE
                    d[len(d)-1][_mon] = int(node.xpath('.//FREE_RIDE_NUM')[0].text) + int(node.xpath('.//FREE_ALIGHT_NUM')[0].text)                    
    for mon in range(1,todaymon):
        _mon = str.format("%d%02d") %(todayyear,mon)
        url = os.path.join('http://openapi.seoul.go.kr:8088/',_key['dataseoul'],_type,_service,_start,_end,_mon)
        url = url.replace('\\','/')
        response = requests.get(url).text
        tree = lxml.etree.fromstring(response.encode('utf-8'))
        nodes = tree.xpath('//row')
        cnt=0;
        for node in nodes:
            NM = node.xpath('.//SUB_STA_NM')[0].text
            LINE = node.xpath('.//LINE_NUM')[0].text
            for cnt,Station in enumerate(d):
                tNM = Station['SUB_STA_NM']
                tLINE = Station['LINE_NUM']
                if NM == tNM and tLINE == LINE:
                    cnt=-1                        
                    Station[_mon] = int(node.xpath('.//FREE_RIDE_NUM')[0].text) + int(node.xpath('.//FREE_ALIGHT_NUM')[0].text)
                    break;
            if cnt!=-1:
                d.append(dict())
                d[len(d)-1]['SUB_STA_NM'] = NM
                d[len(d)-1]['LINE_NUM'] = LINE
                d[len(d)-1][_mon] = int(node.xpath('.//FREE_RIDE_NUM')[0].text) + int(node.xpath('.//FREE_ALIGHT_NUM')[0].text)                    

def SaveMongoDB():
    client = MongoClient()
    db=client.StationDB
    db.drop_collection('StationData')
    for data in d:
        db.StationData.insert_one(data)
def FindMaxStation(date):
    max=0
    StationName=''
    for data in d:      
        if date in data.keys():
            if max < data[date]:
                max = data[date]
                StationName=data['SUB_STA_NM']
    if max!=0:
        print u'최대인 역',StationName
        print u'승객 수',max
    else:
        print u'해당하는 데이터가 없습니다.'
reload(sys)
sys.setdefaultencoding('utf-8')
d=[]
GetData()
SaveMongoDB()
while True:
    print u'지하철 무임승차 인원 정보 시스템'
    print u'1 : 역이름 출력\n2 : 원하는 역 탑승객 검색\n3 : 원하는 날짜에 탑승객이 최대인 역 조회\n4 : 종료'
    code = input()
    if code == 1:
        for Station in d:
            print Station['SUB_STA_NM']
    elif code == 2:
        print u'역이름을 입력하시오.'
        StationName = unicode(repr(raw_input().decode('euc-kr')))
        PrintPersonGraph(StationName)
    elif code == 3:
        print u'원하는 연월을 입력하세요. ex)201501'
        date = input()
        FindMaxStation(unicode(date))
    else:
        break