import datetime
date1=(18,3,1999)
date2=(23,5,2005)
d1=datetime.date(date1[2],date1[1],date1[0])
d2=datetime.date(date2[2],date2[1],date2[0])
print(abs(d1-d2))