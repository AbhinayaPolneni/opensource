n=int(input())
min=-2**31
max=2**31 - 1
sign = -1 if n<0 else 1
n=abs(n)
rev=int(str(n)[::-1])
rev*=sign
if rev<min  or rev>max:
    print("0")
else:
    print(rev)
