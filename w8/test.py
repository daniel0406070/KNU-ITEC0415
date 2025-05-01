def rightTriangle1(N):
    def maxNrest(v1, v2, v3):
        '''
        Return v1 ~ v3 as a 3-tuple, such that the 1st element is the max 
            and the 2nd and 3rd elements are the rest
        '''        
        if v1 >= v2 and v1 >= v3: return v1, v2, v3
        elif v2 >= v1 and v2 >= v3: return v2, v1, v3
        else: return v3, v1, v2
    
    count = 0
    for A in range(1, (N+1)**2 - 1): # Choose A > O
        x1, y1 = A // (N+1), A % (N+1)                 
        for B in range(A + 1, (N+1)**2): # Choose B > A
            x2, y2 = B // (N+1), B % (N+1)
            lmax, l1, l2 = maxNrest(x1**2 + y1**2, x2**2 + y2**2, (x1-x2)**2 + (y1-y2)**2)
            if lmax == l1 + l2: count += 1

    return count

def rightTriangle2(N):
    count = 0
    def originRightAngle(n):
        count = n * n
        return count

    def axisRightAngle(n):
        count = n * n * 2
        return count
    
    def otherTriangle(n):
        count = 0

        def gcd(a, b):
            while b != 0:
                if a > b: a, b = b, a % b
                else: b = b % a
            return a
        
        for i in range(1, n+1):
            for j in range(i, n+1):
                space = j//gcd(i, j)
                x_max = j*j//i + i
                x_min = -(j-n)*j//i*-1 + i
                if x_max > n:
                    x_max = n
                if x_min < 0:
                    x_min = 0

                tmp_cnt = (x_max - i)//space + (i - x_min)//space
                if i != j:
                    tmp_cnt *= 2
                count += tmp_cnt

                # print("i: {}, j: {}, space: {}, x_max: {}, x_min: {}, tmp_cnt: {}".format(i, j, space, x_max, x_min, tmp_cnt))

        return count

    count += originRightAngle(N)
    count += axisRightAngle(N)
    count += otherTriangle(N)
    
    return count



if __name__ == "__main__":
    for i in range(1, 10):
        result = rightTriangle2(i)
        answer = rightTriangle1(i)
        print(i, result, answer)