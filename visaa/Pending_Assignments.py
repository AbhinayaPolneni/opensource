x,y,z=list(map(int,input().split()))
a=int((x*y)/60)
b=z*24
if a<=b:
    print("YES")
else:
    print("NO")
