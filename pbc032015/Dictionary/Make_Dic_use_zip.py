# -*- coding: utf -8 -*-
# """ make dic by zipping together name/value
# """
# names = ['name','age','pay','job']
# values = ['vanoanh',34,40000,'hdw']
# D1 = list(zip(names,values)) # list cac tuple 
# D = dict(zip(names,values)) # dict
# print D

def ZipDic(self,names,values):
	D = dict(zip(name,values))
	return D

D = ZipDic(names =['name','age','pay','job'],values = ['oanh',43,90,'student'] )
print D


	
