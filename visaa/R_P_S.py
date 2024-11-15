a,b=map(str,input().split())
if (a=='P' and b=='R') or (a=='S' and b=='P') or (a=='R' and b=='S'):
    print("Vignesh")
elif (b=='P' and a=='R') or (b=='S' and a=='P') or (b=='R' and a=='S'):
    print("Charan")
else:
    print("NULL")
