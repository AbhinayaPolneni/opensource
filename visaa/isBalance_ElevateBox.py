n=int(input())
a=list(map(int,input().split()))
bal=[]
for i in range(n):
    left=sum(a[:i]) if i>0 else 0
    right=sum(a[i+1:]) if i<n-1 else 0
    bal_sum=abs(left-right)
    bal.append(bal_sum)
print(" ".join(map(str,bal)))
    
