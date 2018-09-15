#! /usr/bin/env python
#-*- coding: utf-8 -*-
import pandas as pd

unames = ['user_id','gender','age','occupation','zip']

users = pd.read_table('movielens/users.dat',sep = '::',header = None,
                      names = unames,engine='python')
rnames = ['user_id','movie_id','rating','timestamp']

ratings = pd.read_table('movielens/ratings.dat',sep ='::',header = None,names = rnames,engine = 'python')


mnames = ['movie_id','title','genres']

movies = pd.read_table('movielens/movies.dat',sep = '::',header = None,
                      names = mnames,engine='python')
print users[:5]
print ratings[:5]
print movies[:5]

data = pd.merge(pd.merge(ratings,users),movies)


mean_ratings = pd.pivot_table(data,'rating',index = 'title',columns
                                ='gender',aggfunc='mean')
##print mean_ratings[:5]