n=int(input())
arr=list(map(int,input().split()))
b=sorted(arr)
for i in range(n):
    if arr[i]==b[i]:
        flag=1
    else:
        flag=0
if flag==1:
    print("true")
else:
    print("false")
