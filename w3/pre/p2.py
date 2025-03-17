def findAllSequenceRecursion(maxSum, min):
    def recur(currentSum, depth):
        i = min
        while currentSum + i <= maxSum:
            sequence[depth] = i
            print(sequence[0:depth+1])
            recur(currentSum + i, depth + 1)
            i += 1

    sequence = [0 for _ in range(maxSum)]
    recur(0, 0)

findAllSequenceRecursion(4, 2)