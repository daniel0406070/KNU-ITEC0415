

def findLongestConsecutivePrimeSum(*sums):    
    maxSum = max(sums)
    prime = [True] * (maxSum+1)
    prime[0] = prime[1] = False
    p = 2

    while p*p <= maxSum:
        if prime[p]:
            for i in range(p*p, maxSum, p): prime[i] = False
        p += 1

    primelist = []
    for i in range(maxSum):
        if prime[i]: primelist.append(i)

    results = []

    def findLongestConsecutivePrimeSumForN(n):
        sum = 2
        currentPos = (0, 0)

        longest = (-1, -1)
        while currentPos[0] < len(primelist):
            while currentPos[1]+1 < len(primelist) and primelist[currentPos[1]+1] + sum < n:
                currentPos = (currentPos[0], currentPos[1]+1)
                sum += primelist[currentPos[1]]

            if currentPos[1] - currentPos[0] + 1 < longest[1]:
                break
            
            
            tmpSum = sum
            tmpPos = currentPos[1]
            while tmpPos > currentPos[0] and tmpPos - currentPos[0] + 1 > longest[1]:
                if prime[tmpSum]:
                    longest = (tmpSum, tmpPos - currentPos[0]+1)
                    break
                tmpSum -= primelist[tmpPos]
                tmpPos -= 1

            sum -= primelist[currentPos[0]]
            currentPos = (currentPos[0]+1, currentPos[1])
            
        if longest[0] == -1:
            longest = (0, 0)
        if longest[1] == 0:
            longest = (0, 0)
        results.append(longest)

    for n in sums:
        findLongestConsecutivePrimeSumForN(n)
    return results
    

if __name__ == "__main__":

    print(findLongestConsecutivePrimeSum(1000000, 5000000, 8000000))