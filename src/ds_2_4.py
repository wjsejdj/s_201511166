
# coding: utf-8
import lxml.html
import requests
from lxml.cssselect import CSSSelector

keyword='비오는'
r = requests.get("http://music.naver.com/search/search.nhn?query="+keyword+"&x=0&y=0")
_html = lxml.html.fromstring(r.text)

sel = CSSSelector('table[summary] > tbody > ._tracklist_move')
# Apply the selector to the DOM tree.
nodes = sel(_html)

_selAlbum= CSSSelector('.album > a')
for node in nodes:
    #print lxml.html.tostring(item)
    _name = node.xpath('.//td[@class="name"]/a/@title')
    _artist = node.xpath('.//td[@class="_artist artist"]//*[@class="ellipsis"]')
    _album=node.xpath('.//*[@class="album"]/a')
    if _name:
        if _artist:
            print _artist[0].text.strip(),
        else:
            print node.xpath('.//a[@href="#"]')[2].text_content(),
        print "---",
        print _name[0],
        print "---",
        print _album[0].text_content()