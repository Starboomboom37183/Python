# -*- coding: utf-8 -*-
from dateutil import parser
from datetime import datetime
import re
rule1= '(.*?)年(.*?)月(.*?)日'
rule2 = r'//.*?;.*?/\*[\s\S]*?\*/.*?(?=\\r\\n)'
c2 = re.compile(rule2)
c1 = re.compile(rule1)
print(c2)
str = r"// this is my;  /* this is a test */       \r\n"
print(c2.search(str))


