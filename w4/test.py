

def findLongestAmicableChain(n):
    divisorSum = [0 for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(2*i, n+1, i):
            divisorSum[j]+=i

    visited = [False for _ in range(n+1)]
    longest_chain = []

    # print(divisorSum)

    def findChain(num):
        chain = []
        while 0< num <= n and not visited[num]:
            visited[num] = True
            chain.append(num)
            num = divisorSum[num]

        for i in range(len(chain)):
            if chain[i] == num:
                return chain[i:]
        return []
    
    for i in range(1, n+1):
        if not visited[i]:
            chain = findChain(i)
            if len(chain) > len(longest_chain):
                longest_chain = chain

    return longest_chain


if __name__ == "__main__":
    print(findLongestAmicableChain(10)) # [6]
    print(findLongestAmicableChain(100)) # [6]
    print(findLongestAmicableChain(1000)) # [220, 284]
    print(findLongestAmicableChain(10000)) # [1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368, 10744, 10856, 12285, 14595, 17296, 18416, 63020, 76084, 79144, 87633, 88730]
    print(findLongestAmicableChain(100000)) # [14316, 19116, 31704, 47616, 83328, 177792, 295488, 629072, 589786]
    print(findLongestAmicableChain(1000000)) # [14316, 19116, 31704, 47616, 83328, 177792, 295488, 629072, 589786]