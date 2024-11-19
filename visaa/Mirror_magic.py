n=int(input())
a=[]
for _ in range(n):
    x=list(map(int,input().split()))
    a.append(x)
res=[i[::-1] for i in a]
for i in res:
    print(" ".join(map(str,i)))
