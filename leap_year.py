year = int (input ('Enter a year (4 digit) : '))
if year % 4 == 0 and year % 100 == 0:
    if year % 400 == 0:
        print(f"{year} is leap year.")
    else:
        print(f"{year} is NOT leap year. ")
elif year % 4 == 0:
    print(f"{year} is leap year.")
else:
    print(f"{year} is NOT leap year. ")