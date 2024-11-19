n=int(input())
a=[]
for _ in range(n):
    x=list(map(int,input().split()))
    a.append(x)
r_sum=[sum(a[i]) for i in range(n)]
c_sum=[sum(a[i][j] for i in range(n)) for j in range(n)]
res=[(r_sum[i]+c_sum[i]) for i in range(n)]
print(' '.join(map(str,res)))
