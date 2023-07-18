number=int(input("Enter your number:"))
factorial=1
for index in range(number,0,-1):
    factorial=index*factorial
print(factorial)
