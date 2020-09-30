weight = int(input("Weight: "))
type= input("(K)g or (L)bs: ").lower()
if type == 'k' :
     convert = weight*2.20
     print(f"Weight in Lbs: {convert}")
elif type =='l':
     convert = weight*0.45
     print(f"Weight in Kg: {convert}")
else :
     print("Invalid")