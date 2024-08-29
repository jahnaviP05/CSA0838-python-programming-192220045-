year=int(input("enter the year:"))
is_leap=(year%4==0 and year%100!=0) or (year%400==0)
print(f"{year} is a leap year." if is_leap else f"{year} is not a leap year.")
