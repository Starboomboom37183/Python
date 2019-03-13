# -*- coding: utf-8 -*-
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
str3 = "wangyong"
str4 = "11"
str5 = "22"

str6 = str2.format(str3,str4,str5)
print(str6)