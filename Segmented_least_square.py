
# coding: utf-8

# In[88]:

import collections
import bisect
import time
from datetime import datetime
import numpy as np

class point(object):
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return str(self.x,self.y)
    
def compute_error(x,y):
    if len(x)==0 and len(y) ==0 :
        total_error = 0 
    n = len(x)
    a = (n*sum(x*y) -sum(x)*sum(y))/(n*sum(x**2)-sum(x)**2)
    b = (sum(y) - a*sum(x))/n
    #print(a)
    #print(b)
    error = y-a*x-b
    total_error = sum(error**2)
    return total_error

def error_matrix(data):
    x =  [i.x for i in data]
    y =  [i.y for i in data]
    x = np.array(x)
    y = np.array(y)
    n = len(x)
    e = []
    for j in range(n):
        inter = []
        for i in range(j+1):
            #print(i,j)
            error = compute_error(x[i:j+1],y[i:j+1])
            inter.append(error)
        e.append(inter)
    return(e)

def  segmented_leat_square(n,error):
    OPT = np.zeros(n)
    opt_segment = np.zeros(n)
    C = 1
    for j in range(0,n):
        beste = 9e999
        besti = -1
        jpre = error[j]
        #list of tuples (a,b,c) for i=0,1,...,j
        #for each possible start i, up to j
        for i in range(0,j+1):
            #get the error assuming using opt to to i-1, and new fit for i..j,
            #with penalty per segment, C
            if (i > 0):
                e = jpre[i] + OPT[i-1] + C
            else:
                e = jpre[i] + C
            #find i with smallest error            
            if (e < beste):
                beste = e
                besti = i
            #create opt entry for j, consisting of min error and list of of (i,j) 
            #this is this a list of (i,j) segments for this j, consisting of
            #the current best (i,j) appended to list from opt[besti-1]
        OPT[j] = beste  
        opt_segment[j] = besti
    #creating the segment    
    temp=np.zeros(n)
    for j in range(1,n):
        if opt_segment[j]!= opt_segment[j-1]:
            temp[j]=temp[j-1]+1
        else:
            temp[j]=temp[j-1]
    return(temp)   
         

    
if __name__ == '__main__':
    data = []
    data.append(point(1,2))
    data.append(point(2,3))
    data.append(point(4,4))
    data.append(point(4,5))
    data.append(point(5,6))
    data.append(point(6,7))
    data.append(point(7,8))
    data.append(point(8,9))
    data.append(point(9,10))
    data.append(point(10,11))
    error = error_matrix(data)
    n=10
    segment=segmented_leat_square(n,error)
    print(segment)
    

