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



MinimalProductSum=[]
def findMinimalProductSum(n):
    '''
    Find all a minimal product number for each k in 2<=k<=n
    '''

    answer = []
    ans=[]
    def recur(currentnum ,currentSum, depth, max_depth ,sequence):
        if max_depth < depth:
            return
        else:
            if currentSum[1] == currentSum[0]+max_depth-depth:
                ans.append(currentSum[1])
                return
            elif currentSum[1] > currentSum[0]+max_depth-depth:
                return
            for i in range(currentnum, n + 1):
                tmp_sequence = sequence.copy()
                tmp_sequence.append(i)
                recur(i, (currentSum[0]+i,currentSum[1]*i), depth + 1, max_depth, tmp_sequence)

    for i in range(len(MinimalProductSum)+2,n+1):
        recur(1, (0,1), 0, i, [])
        ans.sort()
        MinimalProductSum.append(ans[0])
        ans=[]

    return MinimalProductSum[:n]



def findMinimalProductSumDivision(n):
    '''
    Find all product-sum numbers within 2~n, using division trees
    This function is used to evaluate the execution time of findProductSum()
    '''
    def recur(min, number, currentSum, depth):
        for i in range(min, number + 1):
            if number % i == 0:
                sequence[depth] = i
                if depth >= 1 and number == i:                    
                    numFactors = depth + 1 + dividend - (currentSum + i)
                    if numFactors not in dictionary: dictionary[numFactors] = dividend                    
                else: recur(i, int(number / i), currentSum + i, depth + 1)

    assert type(n)==int and n > 0, f"n={n} must be an integer greater than 0"    
    maxProduct = n ** 2
    sequence = [0 for _ in range(maxProduct)]
    dictionary = {}   # (key,value) = (# of factors (k), minimal product-sum number found so far)
    for dividend in range(2, maxProduct + 1):
        recur(2, dividend, 0, 0)

    result = []    
    for i in range(2, n + 1):
        result.append(dictionary[i])
    return result


if __name__ == "__main__":
    print("Correctness test for findProductSum()")
    correct = True

    if sorted(findProductSum(4)) == sorted(['4=2*2=2+2']): print("P ", end='')
    else:
        print("F ", end='')
        correct = False
    
    if sorted(findProductSum(6)) == sorted(['4=2*2=2+2', '6=1*2*3=1+2+3']): print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    if sorted(findProductSum(9)) == sorted(['4=2*2=2+2', '8=1*1*2*2*2=1+1+2+2+2', '6=1*2*3=1+2+3', '8=1*1*2*4=1+1+2+4', '9=1*1*1*3*3=1+1+1+3+3']): print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    if sorted(findProductSum(12)) == sorted(['4=2*2=2+2', '8=1*1*2*2*2=1+1+2+2+2', '12=1*1*1*1*1*2*2*3=1+1+1+1+1+2+2+3', '6=1*2*3=1+2+3', '8=1*1*2*4=1+1+2+4',\
                              '10=1*1*1*2*5=1+1+1+2+5', '12=1*1*1*1*2*6=1+1+1+1+2+6', '9=1*1*1*3*3=1+1+1+3+3', '12=1*1*1*1*1*3*4=1+1+1+1+1+3+4']): print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    if sorted(findProductSum(16)) == sorted(['4=2*2=2+2', '8=1*1*2*2*2=1+1+2+2+2', '16=1*1*1*1*1*1*1*1*2*2*2*2=1+1+1+1+1+1+1+1+2+2+2+2',\
                              '12=1*1*1*1*1*2*2*3=1+1+1+1+1+2+2+3', '16=1*1*1*1*1*1*1*1*2*2*4=1+1+1+1+1+1+1+1+2+2+4', '6=1*2*3=1+2+3',\
                                 '8=1*1*2*4=1+1+2+4', '10=1*1*1*2*5=1+1+1+2+5', '12=1*1*1*1*2*6=1+1+1+1+2+6', '14=1*1*1*1*1*2*7=1+1+1+1+1+2+7',\
                                    '16=1*1*1*1*1*1*2*8=1+1+1+1+1+1+2+8', '9=1*1*1*3*3=1+1+1+3+3', '12=1*1*1*1*1*3*4=1+1+1+1+1+3+4',\
                                         '15=1*1*1*1*1*1*1*3*5=1+1+1+1+1+1+1+3+5', '16=1*1*1*1*1*1*1*1*4*4=1+1+1+1+1+1+1+1+4+4']): print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    print()
    print()

    print("Correctness test for findMinimalProductSum()")
    correct = True
    for n in range(2, 52):        # test for n = 2 ~ 51
        if findMinimalProductSum(n) == findMinimalProductSumDivision(n): print("P ", end='')
        else:
            print("F ", end='')
            correct = False
            print(f"findMinimalProductSum({n}) differs from findMinimalProductSumDivision({n})")
            print(f"findMinimalProductSum({n}): {findMinimalProductSum(n)}")
            print(f"findMinimalProductSumDivision({n}): {findMinimalProductSumDivision(n)}")
            print()

    print()
    print()
    print("Speed test for findMinimalProductSum()")
    if not correct: print("fail (since the algorithm is not correct)")
    else:        
        n = 100
        tSubmittedCode = timeit.timeit(lambda: findMinimalProductSum(10), number=n)/n        
        tDivSqrt = timeit.timeit(lambda: findMinimalProductSumDivision(10), number=n)/n        
        print(f"Average running time for the submitted code ({tSubmittedCode:.10f}) and the code based on division/3 ({tDivSqrt/3:.10f})")        
        if tSubmittedCode * 3 < tDivSqrt: print("pass")
        else: print("fail")

        print()
        print(f"Average running time for the submitted code ({tSubmittedCode:.10f}) and the code based on division/8 ({tDivSqrt/8:.10f})")        
        print("optional: ", end='')
        if tSubmittedCode * 8 < tDivSqrt: print("pass")
        else: print("fail")
    print()
