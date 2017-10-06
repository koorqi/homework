import time
import datetime
def get_days_to_new_year():
	now=datetime.date.today() 
	ny=now.replace(now.year+1,1,1) 
	return (ny - now).days 

#print (get_days_to_new_year())



