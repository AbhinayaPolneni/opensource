s=input()
c=0
c1=0
x="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
for i in s:
    if i in {'a','e','i','o','u','A','E','I','O','U'}:
        c+=1
    elif i in x:
        c1+=1
print(f"{c},{c1}")
