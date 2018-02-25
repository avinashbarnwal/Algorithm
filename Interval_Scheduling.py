
# coding: utf-8

# In[35]:

import collections
from datetime import datetime
import time
import bisect

class Interval(object):
    '''Date weighted interval'''

    def __init__(self, title, start, finish):
        self.title  = title
        self.start  = int(time.mktime(datetime.strptime(start,'%m/%d/%Y').timetuple()))
        self.finish = int(time.mktime(datetime.strptime(finish,"%m/%d/%Y").timetuple()))
                
def schedule_unweighted_intervals(I):
    #For every interval j, compute the rightmost mutually compatible interval i, where i < j
    #   I is a sorted list of Interval objects (sorted by finish time)
    
    I.sort(lambda x,y: x.finish-y.finish)
    # extract start and finish times
    
    start = [i.start for i in I]
    finish = [i.finish for i in I]
    o =[]
    finish = 0
    j=0
    for i in I:
        if finish <= i.start:
            print(I[j])
            finish=i.finish
            o.append(i)
    return o    
if __name__ == '__main__':
    I = []
    I.append(Interval("Summer School" , "01/14/2017", "02/24/2017"))
    I.append(Interval("Semester 1"    , "03/01/2013", "06/04/2013"))
    I.append(Interval("Semester 2"    , "08/18/2013", "11/24/2013"))
    I.append(Interval("Trimester 1"   , "03/22/2013", "05/16/2013"))
    I.append(Interval("Trimester 2"   , "05/22/2013", "07/24/2013"))
    I.append(Interval("Trimester 3"   , "08/28/2013", "11/16/2013"))
#datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
    p=schedule_unweighted_intervals(I)
    print(p)

