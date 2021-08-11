# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 17:23:19 2021

@author: NiharikaSrivastava
"""
from functools import reduce

names=['java','javascript','kotlin','python','groovy']

orders =[{'id':1,'name':'Iphone','price':5678.5},
         {'id':3,'name':'Ipad','price':3678.5},
         {'id':4,'name':'macbook','price':123678.5}]

for x in names:
    if x.startswith('j'):
        print(x)
        
def starts_with_j(val): 
    return val.startswith('j')

print(list(filter(starts_with_j,names)))


print(list(filter(lambda order: order['price'] >= 50000,orders)))
"""
def avg(res):
    sum1=0
    count=1
    count=count+1
    return (sum1+res)/count
"""
# =============================================================================
# res ={sub['price'] for sub in orders}
#         
# print(max(res))
# print(min(res))
# print(sum(res))
# 
# =============================================================================
# =============================================================================
# print(reduce(lambda o1,o2:o1+o2,map(lambda orders:orders['price'],filter(lambda orders: orders['price']>=50000,orders))))
# 
# count=0
# for x in orders:
#     count=count+1
#     # x.values()==True
# print(count)
# 
# 
# def average():
#     count=0
#     sum1=0
#     for x in orders:
#         sum1=sum1+x['price']
#         count=count+1
#     print(sum1/count)
#     
# average()
# 
# 
#     
# res ={sub['price'] for sub in orders}
# print(sum(res)/len(res))
# 
# 
# =============================================================================

print(range(5))

for i in range(5,10):
    print(i)
    
print(list(range(0,10,2)))




