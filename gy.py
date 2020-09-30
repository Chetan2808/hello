weight = int(input("Weight:"))
x= input("(L)bs or (K)g:")
if x.upper()=='K':
    weight = weight*2.20
    print(f'You are {weight} pounds.')
elif x.upper()=='L':
    weight= weight*0.45
    print(f'You are{weight}kgs.')
else:
    print("Invalid ")