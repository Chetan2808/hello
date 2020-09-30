S = int(input())
W = int(input())
E = int(input())
i = 0
for i in range(S,E+1,W):
    print(i,int((i-32)*5/9),S*E*W-"\t_")