# coding: utf-8
import lxml.html
from lxml.cssselect import CSSSelector
import re
import requests
from lxml import etree

r = requests.get('http://www.ieee.org/conferences_events/conferences/search/index.html')

html = lxml.html.fromstring(r.text)
p = re.compile('href="(http://.*?)"')
nodes = p.findall(r.text)
print "<regex>"
for node in nodes:
    print node
    print "----------"

_htmltree = etree.HTML(r.text)
nodes = _htmltree.xpath('//*[@id="inner-container"]//table//p//*[@href]')
print "\n<lxml>\n"
for node in nodes:
    print node.text
    print "----------"

sel=CSSSelector('div.content-r-full table.nogrid-nopad tr p>a[href]')
nodes = sel(html)
print "\n<cssselect>\n"
for node in nodes:
    print node.text
    print "----------"