import os
import shutil

input = open("test/1.txt","r")
a = set()
for line in input:
    a.add(line.strip())

for file in a:
    if file[0:24]=0="/home/wangyong/wangyong/":
        newstr = "/home/wangyong/wangyong/test2/"+file[30: ]
        print newstr
        shutil.copy(newstr,file)
input.close()

while True:
    print "haha"
