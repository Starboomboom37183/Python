#! /usr/bin/env python
#-*- coding: utf-8 -*-
from urllib import urlopen
from bs4 import BeautifulSoup

text = urlopen('http://python.org/community/jobs').read()
#text = urlopen('http://www.baidu.com').read()
soup = BeautifulSoup(text)

print soup.prettify()
jobs = set()

print soup('a')
##print soup.a
for header in soup('h3'):
    links = header('a','reference')
    print links
    if not links:continue
    link = links[0]
    jobs.add('%s (%s)' %(link.string,link['href']))

print '\n'.join(sorted(jobs,key = lambda s:s.lower()))

