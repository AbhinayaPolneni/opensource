n=int(input())
for i in range(1,n+1):
    inc=''.join(str(x) for x in range(1,i+1))
    dec=''.join(str(x) for x in range(i,0,-1))
    spaces=' '*(2*(n-i))
    print(inc+spaces+dec)
