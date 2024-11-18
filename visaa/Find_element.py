n=int(input())
a=list(map(int,input().split()))
k=int(input())
flag=0
for i in range(n):
    if a[i]==k:
        flag=1
        x=i
        break
if flag==1:
    print(x)
else:
    print("-1")
