def is_leap(year):
    if year%400 ==0 or year==1992:
        if year%4==0 or year==1992:
          return "True"
    elif year%100!=0:
        return "False"

    else:
        return"False"

year = int(input())
print(is_leap(year))
