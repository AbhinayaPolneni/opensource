x,n=map(int,input().split())
y=x*100
if n<=y:
    print(0)
else:
    z=n-y
    print((z+99)//100)
