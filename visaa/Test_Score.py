n,x,y=list(map(int,input().split()))
if n*x>=y and y%x==0:
    print("YES")
else:
    print("NO")
