#confing: utf-8
from urllib import FancyURLopener
import re
import urllib2
class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0'
keyword ="python"
myopener = MyOpener()
page = myopener.open('http://www.google.com/search?q='+keyword)
html=page.read()
p=re.compile('href="(https://.*?)"')
#p=re.compile('.*href.*')
res=p.findall(html)
print '<Keyword = Python>'
for i,item in enumerate(res):
    print i,item
keyword = 'c'
page = myopener.open('http://www.google.com/search?q='+keyword)
html = page.read()
res = p.findall(html)
print '<Keyword = C>'
for i,item in enumerate(res):
    print i,item