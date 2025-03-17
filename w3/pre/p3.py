def findAllSequenceNoRecursion(maxSum, min):
    sequence = [0 for _ in range(maxSum)]
    currentSum = [0 for _ in range(maxSum+1)] # currentSum in the stack
    i = [0 for _ in range(maxSum+1)] # i in the stack
    i[0] = min
    depth = 0

    while True:
        while currentSum[depth] + i[depth] > maxSum: # 함수 반환 시뮬레이션하는 루프
            depth -= 1
            if depth < 0: return # 루트 이전까지 돌아가는 것은 더는 탐색할 수열 없음 의미
        sequence[depth] = i[depth] # 이번에 선정한 숫자 i를 수열에 추가
        print(sequence[0:depth+1]) # 선정한 수열 출력
        currentSum[depth+1] = currentSum[depth] + i[depth] # 다음 depth의 합 증가
        i[depth] += 1 # 현재 depth로 반환 시 다음 값 사용하도록 i 값을 미리 증가시켜둠
        depth += 1 # 다음 depth로 이동
        i[depth] = i[depth-1] # 새 depth에서는 i를 초깃값 min부터 시작

findAllSequenceNoRecursion(6, 2)