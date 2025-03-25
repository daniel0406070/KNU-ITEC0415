
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

    for i in range(len(MinimalProductSum)+2,n):
        recur(1, (0,1), 0, i, [])
        ans.sort()
        MinimalProductSum.append(ans[0])
        ans=[]

    return MinimalProductSum[:n-1]

if __name__ == '__main__':
    print(findMinimalProductSum(40))