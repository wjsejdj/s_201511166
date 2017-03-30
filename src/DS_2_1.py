# coding: utf-8
import requests
import re
rResponse = requests.get('http://python.org')
_html = rResponse.text
p = re.compile('href="(http://.*?)"')
nodes = p.findall(_html)
print "http url count ",len(nodes),"-------------"
for i ,node in enumerate(nodes):
        print i,node
p = re.compile('<h1>(.*?)</h1>')
nodes = p.findall(_html)
print "<h1> tags count ",len(nodes),"--------------"
for i, node in enumerate(nodes):
    print i,node
p = re.compile('<p>(.*?)</p>')
nodes = p.findall(_html)
print "<p> tags count ",len(nodes),"---------------"
for i,node in enumerate(nodes):
    print i,node