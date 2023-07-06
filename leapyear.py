from types import LambdaType
def leap(year):
   return year

year = int(input())
if (year%4==0 ) and (year%100!=0):
  print('true')
elif(year%400==0) and (year%100==0):
  print('true')
else:
  print('false')
  