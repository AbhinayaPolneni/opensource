n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in range(1,n):
    l.append(arr[i])
l.append(arr[0])
print(" ".join(map(str,l)))
