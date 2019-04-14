# -*- coding: utf-8 -*-
input = open("Dijkstra.c","r")
lines = input.read()
input.close()
count = 0
start = 0
end = 0
i = 0
output = open("Dijkstra.c","w")
while i<len(lines):
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
            pos= lines.rfind("\n",0,start)
            length = start - pos
            if len(temp)>1:
                print(temp)
                line_replace = ""
                for i in range(1,len(temp)):
                    temp[i]=" "*length+temp[i].lstrip()
                for s in temp:
                    line_replace = line_replace+s+"\n"
                lines = lines[:start]+line_replace+lines[end:]
                i = start + len(line_replace)+1

    i+=1
output.write(lines)
output.close()

