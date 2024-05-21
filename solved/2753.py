yun_year = int(input())

if yun_year % 4 == 0:
    if yun_year % 100 != 0:
        print("1")
    elif yun_year % 400 == 0:
        print("1")
    else:
        print(("0"))
else:
    print("0")