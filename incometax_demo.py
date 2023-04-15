'''

income

  income  <100000    0%
  income  >100000      < 300000    10%
  income  >300000      <1000000     20%
  income  >1000000                 30%


income 80000    Tax : 0
income 120000   Tax : 2000
income 340000   Tax : 20000+8000  28000
income 150000  Tax
        income tax calculate
'''
income=int(input("Enter Income:"))
tax=0
if income<100000:
    print("Tax :",tax)
elif 100000<=income<=300000:
   tax=(income%100000)*0.10
   print("Tax :",tax)
elif 300000<=income<=1000000:
   tax=20000+((income%300000)*0.20)
   print("Tax:",tax)
elif income>1000000:
    tax=20000+140000+((income%1000000)*0.40)
    print("Tax:",tax)





