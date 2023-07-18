User=input("Enter a string:")
for i in range(len(User)):
    for j in range(i,len(User)):
        print(User[i:j+1])
