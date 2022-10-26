a=list(map(int,input().split(",")))
ans=[]
for i in a:
    x = 0
    for j in range(1,i+1):
        if i%j==0:
            x+=j
    if x in a:
        ans.append(i)
ans.sort()
if len(ans) == 0:
    print(-1)
else:
    print(*ans)
        