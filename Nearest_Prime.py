t = int(input())
for i in range(t):
    n = int(input())
    next_prime=n
    while True:
        fc=0
        for j in range(1,next_prime+1):
            if next_prime%j==0:
                fc+=1
        if fc==2:
            break
        next_prime+=1
    pre_prime=n
    while True:
        fc=0
        for b in range(1,pre_prime+1):
            if pre_prime%b==0:
                fc+=1
        if fc==2:
            break
        pre_prime-=1
    if n - pre_prime <= next_prime - n:
        print(pre_prime)
    else:
        print(next_prime)
    
        
     
        