import datetime

def FormatDateTime(DateTime=0):
     if DateTime==0:
         x=datetime.datetime.now()
         now=x.strftime('%d %B %Y %X')
         return now
     else:
         z=DateTime
         y=datetime.datetime.strptime(z,"%Y-%m-%d")
         now=y.strftime('%d %B %Y %X')
         return now
