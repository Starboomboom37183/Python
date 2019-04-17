#! /usr/bin/env python
#-*- coding: utf-8 -*-

def lines(file):
    for line in file:
        yield line
    yield '\n'

def blocks(file):
    block = []
    ##a = list(lines(file))
    for line in lines(file):
        #print line
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []

file = open('listing20-1.txt','r')
print list(lines(file))  #到了文件的末尾了
file.seek(0)
print list(blocks(file))
file.close()