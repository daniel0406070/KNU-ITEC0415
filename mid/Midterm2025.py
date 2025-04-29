import timeit
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
    phi = [i for i in range(N+1)]

    for i in primenums:
        for j in range(i,N+1, i):
            phi[j] = phi[j] * (i-1) // i


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
            if chains[j]!=0:
                chains[i][0]+=chains[j][0]
                chains[i][1].extend(chains[j][1])
                break
            chains[j][0]+=j
            chains[j][1].append([j])
        
    for i in range(2,N+1):
        # print(chains[i])
        if chains[max][0] < chains[i][0]:
            max = i




    return (max,chains[max][0],chains[max][1])


def speedCompare(N):
    for n in range(2, N + 1):        
        if n % 2 == 0:
            while n % 2 == 0: n //= 2
        
        p = 3
        while p * p <= n:
            if n % p == 0:
                while n % p == 0: n //= p
            p += 2


if __name__ == "__main__":  
    print("Correctness test for midterm2025()")
    print("For each test case, if your answer does not appear within 5 seconds, then consider that you failed the case")    
    correct = True
    
    if midterm2025(10) == (9, 18, [9, 6, 2, 1]): print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    if midterm2025(100) == (97, 256, [97, 96, 32, 16, 8, 4, 2, 1]): print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    if midterm2025(1000) == (983, 2702, [983, 982, 490, 168, 48, 16, 8, 4, 2, 1]): print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    if midterm2025(10000) == (9839, 29212, [9839, 9838, 4918, 2458, 1228, 612, 192, 64, 32, 16, 8, 4, 2, 1]): print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    if midterm2025(100000) == (98999, 291618, [98999, 98998, 49498, 24748, 11792, 5280, 1280, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]): print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    if midterm2025(1000000) == (982559, 2926834, [982559, 982558, 491278, 245638, 122818, 61408, 28800, 7680, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]): print("P ", end='')
    else:
        print("F ", end='')
        correct = False
    
    print()
    print()
    print("Speed test for midterm2025()")    
    if not correct: print("fail (since the algorithm is not correct)")
    else:
        repeat = 10
        N = 10000
        tSpeedCompare = timeit.timeit(lambda: speedCompare(N), number=repeat)/repeat
        tSubmittedCode = timeit.timeit(lambda: midterm2025(N), number=repeat)/repeat    
        print(f"For input N = {N}")
        print(f"Average running times of the submitted code and speedCompare*2: {tSubmittedCode:.10f} and {tSpeedCompare*2:.10f}")    
        if tSubmittedCode < tSpeedCompare * 2: print("pass")
        else: print("fail")
        print()

        print(f"Average running times of the submitted code and speedCompare: {tSubmittedCode:.10f} and {tSpeedCompare:.10f}")    
        if tSubmittedCode < tSpeedCompare: print("pass")
        else: print("fail")
        print()
