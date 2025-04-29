import math

primenums = []
def getprimenums(N):
    global primenums
    primes = [1 for _ in range(N+1)]
    primes[0] = 0
    primes[1] = 0
    for i in range(2, int(math.sqrt(N))+1):
        if primes[i]:
            for j in range(2*i,N+1,i):
                primes[j] = 0

    primenums = []
    for i in range(len(primes)):
        if primes[i]:
            primenums.append(i)

phi = []

def getphi(N):
    global primenums
    nums=[]

    if (phi[N]):
        return phi[N]
    
    n=N

    result=N
    for i in primenums:
        if n == 1:
            break
        if n%i == 0:
            while n%i == 0:
                n//=i
            result -= result//i
            
    phi[N] = result
    return result

    

def getphis(N):
    global phi
    global primenums
    phi = [0 for _ in range(N+1)]

    # def recur(num,N,sel,tphi):
    #     if num>N:
    #         return
        
    #     phi[num]=tphi
        
    #     if sel != -1:
    #         recur(num*primenums[sel],N,sel,tphi*primenums[sel])
    #     for i in range(sel+1,len(primenums)):
    #         recur(num*primenums[i],N,i,tphi*(primenums[i]-1))
        
    # recur(1,N,-1,1)
        
    for i in range(1, N+1):
        phi[i] = getphi(i)


def midterm2025(N):
    global primenums
    global phi
    global chains
    getprimenums(N)
    getphis(N)

    chains = [0 for _ in range(N+1)]
    chains[1] = [1,[1]]
    max = 1
    for i in range(2,N+1):
        j = i
        chains[i] = [i,[i]]
        while j != 1:
            j=phi[j]
            chains[j][0]+=j
            chains[j][1].append([j])
        
    for i in range(2,N+1):
        # print(chains[i])
        if chains[max][0] < chains[i][0]:
            max = i




    return (max,chains[max][0],chains[max][1])

if __name__ == "__main__":
    print(midterm2025(1000000))