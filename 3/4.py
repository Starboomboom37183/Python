# -*- coding: utf-8 -*-
import re
input = open("Dijkstra.c","r")
lines = input.read()
input.close()
count = 0
start = 0
end = 0
i = 0
def skip_this(lines,i):
    i +=1
    while i < len(lines):
        if lines[i]=="\"":
            if lines[i-1]!="\\\\":
                return i
        i+=1



output = open("Dijkstra.c","w")
while i<len(lines):
    if lines[i] == "\"":
        t1 = i
        i = skip_this(lines,i)
        i+=1
        continue
    if lines[i]=="(":
        if count ==0:
            start = end = i
        count+=1
    elif lines[i]==")":
        if count==0:
            break
        count-=1
        if count==0:
            end = i+1
            temp = lines[start:end].splitlines()
            if len(temp)>1:
                pos = lines.rfind("\n", 0, start)
                for k in range(start + 1, end):
                    if lines[k] != " ":
                        break
                tab_num = len(re.findall("\t", lines[pos:k]))
                length = k - pos - 1 + 3 * tab_num
                line_replace = ""
                for i in range(1,len(temp)):
                    temp[i]=" "*length+temp[i].lstrip()
                for s in temp:
                    line_replace = line_replace+s+"\n"
                lines = lines[:start]+line_replace.rstrip()+lines[end:]
                i = start + len(line_replace)+1

    i+=1
output.write(lines)
output.close()

