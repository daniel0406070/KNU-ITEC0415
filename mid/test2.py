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
def getphis(N):
    global phi
    global primenums
    phi = [i for i in range(N+1)]

    for i in primenums:
        for j in range(i,N+1, i):
            phi[j] = phi[j] * (i-1) // i



if __name__ == "__main__":
    getprimenums(1000)
    getphis(1000)
    print(phi)