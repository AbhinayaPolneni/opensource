n=int(input())
a=list(map(int,input().split()))
def check(n,a):
    for i in range(n-1):
        if a[i]>a[i+1]:
            return "false"
    return "true"
print(check(n,a))
