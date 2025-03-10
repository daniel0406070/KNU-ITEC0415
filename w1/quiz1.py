def findAllSequence1(maxSum, min):

    def recur(min, currentSum, depth):

        while currentSum + min <= maxSum:

            sequence[depth] = min

            print(sequence[0:depth+1])

            recur(min, currentSum + min, depth + 1)

            min += 1

 

    assert maxSum > 0, f"maxSum = {maxSum} must be greater than 0"

    assert min > 0, f"min = {min} must be greater than 0"

    sequence = [0 for _ in range(maxSum)]

    recur(min, 0, 0)

 

if __name__ == "__main__":

    findAllSequence1(6, 2)