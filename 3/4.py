# -*- coding: utf-8 -*-
input = open("Dijkstra.c","r")
lines = input.read()
count = 0
start = 0
end = 0
i = 0
while i<len(lines):
    if lines[i]=="(":
        if count ==0:
            start = end = i
        count+=1
    elif lines[i]==")":
        if count!=0:
            count-=1
            if count==0:
                end = i+1
        else:
            print("error")
    if count==0 and start!=end:
        str1 = lines[start:end]

    i+=1


