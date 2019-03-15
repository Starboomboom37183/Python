# -*- coding: utf-8 -*-
from dateutil import parser
from datetime import datetime
import re
rule1= '(.*?)年(.*?)月(.*?)日'
c1 = re.compile(rule1)
try:
    time_str = "2018.9.3"
    match =  c1.search(time_str)
    if match:
        time_str = match.group(1)+"-"+match.group(2)+"-"+match.group(3)
    dtime = parser.parse(time_str)
    str = dtime.strftime("%Y-%m-%d")
    print(str)
except:
    print(time_str)
