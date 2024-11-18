n=int(input())
k=int(input())
bit=2**(k-1)
if n&bit !=0:
    print("true")
else:
    print("false")
