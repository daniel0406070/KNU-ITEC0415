import timeit

def createProductSumSequence(sequence, maxIndex):
    '''
    Create a product-sum string given a sequence of numbers (e.g., createProductSumSequence([2,3], 1) --> '6=1*2*3=1+2+3')

    Input:
        sequence -- list of integers
        maxIndex -- maximum index to use for sequence (i.e., sequence[0] ~ sequence[maxIndex] are used to create the string)
    '''
    result = []

    product = 1
    sum = 0
    for i in range(maxIndex + 1): 
        product *= sequence[i]
        sum += sequence[i]

    result.append(f"{product}=")
    for i in range(product - sum): result.append("1*")
    for i in range(maxIndex + 1):
        result.append(str(sequence[i]))            
        if i < maxIndex: result.append("*")
    result.append("=")
    for i in range(product - sum): result.append("1+")
    for i in range(maxIndex + 1):
        result.append(str(sequence[i]))            
        if i < maxIndex: result.append("+")

    return ''.join(result)


def findProductSum(n):
    '''
    Find all product-sum numbers within 2~n
    '''    
    factorization = [0 for _ in range(n + 1)]
    for i in range(2, n + 1):
        factorization[i] = [i]

    for i in range(2, n + 1):
        for j in range(i * 2, n + 1, i):
            factorization[j].append(i)
        factorization[i].sort(reverse=True)

    ans=[]

    def recur(number, currentnum ,currentSum, depth, sequence):
        if currentSum[0]>currentSum[1]:
            return
        
        if currentSum[1] == number:
            if len(sequence) > 1:
                ans.append(sorted(sequence))
            return
        
        if currentSum[1] > number:
            return
        
        for i in factorization[number]:
            if i > currentnum:
                continue
            tmp_sequence = sequence.copy()
            tmp_sequence.append(i)
            recur(number, i, (currentSum[0]+i,currentSum[1]*i), depth + 1, tmp_sequence)

    for i in range(2, n + 1):
        recur(i, i, (0,1), 0, [])

    answer = []
    for sequence in ans:
        answer.append(createProductSumSequence(sequence, len(sequence) - 1))

    return answer

if __name__ == '__main__':
    print(findProductSum(9))