# coding: utf-8
import requests
from lxml.cssselect import CSSSelector
import lxml.html

def getkleague():
    print '<Get Kleague>'
    r = requests.get('http://www.kleague.com/')
    html = lxml.html.fromstring(r.text)
    sel = CSSSelector('div#modal_classic-team-rank table tbody tr')
    nodes = sel(html)
    print u"테이블 행 갯수: ", len(nodes)
    counter=0
    for teams in nodes:
        for cols in teams:
            if cols.xpath('.//a/text()'):
                print cols.xpath('.//a/text()')[0],
            elif cols.xpath('.//span/text()'):
                print cols.xpath('.//span/text()')[0],
            else:
                print cols.text.strip(),
        print

def getkb():
    r = requests.get('http://www.kbreport.com/main')
    _htmlTree = lxml.etree.HTML(r.text)
    nodes = _htmlTree.xpath("//div[@class='team-rank-box']//table[@class='team-rank']//tr")
    print u"테이블 행 갯수: ", len(nodes)
    counter=0
    for teams in nodes:
        for cols in teams:
            if cols.xpath('.//a/text()'):
                print cols.xpath('.//a/text()')[0],
            else:
                print cols.text.strip(),
        print

def main():
    getkleague()
    getkb()

if __name__ == "__main__":
    main()