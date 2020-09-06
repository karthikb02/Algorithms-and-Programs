N=int(input())
sieve=[False for ctr in range(N+1)]
ctr=2
while ctr*ctr<=N:
    if not sieve[ctr]:
        m=ctr*ctr
        while m<=N:
            sieve[m]=True
            m+=ctr
    ctr+=1
for ctr in range(2,N+1):
    if not sieve[ctr]:
        print(ctr,end=" ")


                
    
