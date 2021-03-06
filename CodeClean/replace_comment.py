# -*- coding: utf-8 -*-
import os, sys,string,re,glob
str1=u'''/*
 *Copyright (c) Huawei Technologies Co.,Ltd.2012-2019,All rights reserved
 *Description:{}
 *Author:{}
 *Create:{}
*/ 
'''
str2=u'''/*
*Description:{}
*Author:{}
*Date:{}
*/
'''

Rule1 = '\/\*[\s\S]*?\*\/'
c1=re.compile(Rule1)
def usage():
    print(u'''
    help: del_comment.py <filename | dirname>\n
       ''')

def deal_file(src):
     # file exist or not
    if not os.path.exists(src):
         print('Error: file - %s doesn\'t exist.\n'% src)
         return False
    if os.path.islink(src):
         print('Error: file - %s is a link.')
         return False
    filetype = (os.path.splitext(src))[1]
    if not filetype in ['.c','.h']:
        return False
    try:
         if not os.access(src, os.W_OK):
             os.chmod(src,stat.S_IWRITE)
    except:
           print('Error: you can not change %s\'s mode.\n'% src)

    inputf = open(src, 'r')
    outputfilename= (os.path.splitext(src))[0] + '_no_comment'+filetype
    outputf = open(outputfilename, 'w')

    lines=inputf.read()
    inputf.close()
    comment = re.findall(Rule1,lines)
    print(comment)
    for s in comment:
        match1 = re.search(r'Author\s*?:(.*?)\n',s)
        match2 = re.search(r'Mail\s*?:(.*?)\n',s)
        match3 = re.search(r'Created\s*?Time\s*?:(.*?)\n', s)
        if match1 and match2 and match3:
            str3 = str2.format(match1.group(1),match2.group(1),match3.group(1))
        lines = re.sub(Rule1,str3, lines)
    outputf.write(lines)
    outputf.close()
    return True

#--------------------------------------------------------------
def deal_dir(src):
    if not os.path.exists(src):
        print('Error: dir - %s is not exist.\n'%s (src))
        return False
    filelists = os.listdir(src)
    for eachfile in filelists:
        eachfile = src + '/' +eachfile
        if os.path.isdir(eachfile):
            deal_dir(eachfile)
        elif os.path.isfile(eachfile):
            deal_file(eachfile)
    return True

#--------------------------------------------------------------
def main():
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)
    src = sys.argv[1]
    if os.path.isdir(src):
        dire = os.path.abspath(src)
        dirFlag = True
    elif os.path.isfile(src):
        fl = os.path.abspath(src)
        dirFlag = False
    else:
        print('File input error\n')

    if dirFlag:
            deal_dir(dire)
    else:
            deal_file(fl)
            print('Successful handle file.\n')

#--------------------------------------------------------------

if __name__ == '__main__':
    deal_file(sys.argv[1])