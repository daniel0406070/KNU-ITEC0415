import math

def totientMaximum3(*Ns):
    maxN = max(Ns) # Find the maximum N in the input list

    primes = [1] * (maxN + 1) # Create a list to store prime numbers
    primes[0] = 0
    primes[1] = 0

    for i in range(2, maxN + 1):
        if primes[i]:
            for j in range(i * 2, maxN + 1, i):
                primes[j] = 0

    primes = [i for i in range(maxN + 1) if primes[i]] # Filter out non-prime numbers

    res = []

    for n in Ns:
        res_n = 1
        res_ntotient_upper = 1
        res_ntotient_lower = 1

        for i in range(len(primes)):
            if primes[i] * res_n > n:
                break
            res_n *= primes[i]
        
        for j in range(i+1):
            res_ntotient_upper *= primes[j]
            res_ntotient_lower *= primes[j] - 1

        res.append(res_ntotient_upper / res_ntotient_lower)
    
    return res

def findmaxprimemut(n):
    primes = [2]
    i = 3
    result = 2
    while True:
        if i > n:
            break
        for p in primes:
            if i % p == 0:
                break
        else:
            if result*i > n:
                break
            primes.append(i)
            result *= i
            
        i += 2

    return result

def primeslessthan(n):
    primes = [1] * n
    primes[0] = 0
    primes[1] = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i]:
            for j in range(i * 2, n, i):
                primes[j] = 0

    primes = [i for i in range(n) if primes[i]] # Filter out non-prime numbers
    return max(primes)

def totientMinimum(*Ns):    
    maxNs = max(Ns) # Find the maximum N in the input list

    primes = [1] * (maxNs+1)
    primes[0] = 0
    primes[1] = 0
    for i in range(2, int(math.sqrt(maxNs)) + 1):
        if primes[i]:
            for j in range(i * 2, maxNs, i):
                primes[j] = 0

    primes = [i for i in range(maxNs+1) if primes[i]] # Filter out non-prime numbers
    primes.sort(reverse=True) # Sort the primes in descending order

    res = []
    for n in Ns:
        for prime in primes:
            if prime <= n:
                res.append(prime)
                break
            
    return res


            


if __name__ == "__main__":
    # Test the function with a list of N values
    # result = totientMaximum3(10, 20, 30)
    result = totientMinimum(100000, 500000, 1000000)
    print(result)