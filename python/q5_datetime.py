# Hint:  use Google to find python function

####a) 
from datetime import datetime

date_start = '01-02-2013'
date_stop = '07-28-2015'

def elapsed_time_nd(date_start, date_stop):
    start = datetime.strptime(date_start, '%m-%d-%Y')
    end = datetime.strptime(date_stop, '%m-%d-%Y')
    print(abs((start-end).days))
    return abs((start-end).days)   

####b)  

date_start = '12312013'  
date_stop = '05282015'  

def elapsed_time_n(date_start, date_stop):
    start = datetime.strptime(date_start, '%m%d%Y')
    end = datetime.strptime(date_stop, '%m%d%Y')
    return abs((start-end).days)

####c)  

date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

def elapsed_time_abbrd(date_start, date_stop):
    start = datetime.strptime(date_start, '%d-%b-%Y')
    end = datetime.strptime(date_stop, '%d-%b-%Y')
    return abs((start-end).days)
