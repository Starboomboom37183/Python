#! /usr/bin/env python
#-*- coding: utf-8 -*-
def conflict(state,nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0,nextY-i):
            return True
    return False

def quenes(num=8,state = ()):
    for pos in range(num):
        if not conflict(state,pos):
            if len(state)==num-1:
                yield (pos,)
            else:
                for result in quenes(num,state+(pos,)):
                    yield (pos,)+result


def prettyprint(solution):
    def line(pos,len = len(solution)):
        return '*'*pos+'X'+'*'*(len-pos-1)
    for pos in solution:
        print line(pos)

def printAll(L):
    for i in xrange(len(L)):
        print '第%d种情况:' %(i+1)
        prettyprint(L[i])
        print '=================='

size = raw_input("请输入棋盘大小: ")
printAll(list(quenes(int(size))))