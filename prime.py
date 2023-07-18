def If_Prime(number):
    if (number==2):
        return "Prime"
    if(number==0 or number== 1):
        return "Not Prime"
    for divisor in range(2,number):
        if(number%divisor==0):
            return "Not Prime"
    return "Prime"



def List_of_prime():
    for i in range(0,101):
        if(If_Prime(i)=="Prime"):
            print(i)
List_of_prime()
