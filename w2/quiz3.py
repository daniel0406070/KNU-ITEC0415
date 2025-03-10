coin=[]

def coin_35(n):
    if n==0 or n==1 or n==2 or n==4 or n==7:
        return [(0,0)]
    
    coin_n=set()
    
    for i in range(0, len(coin[n-3])):
        if (coin[n-3][i][0]+1)*3+(coin[n-3][i][1])*5==n:
            coin_n.add((coin[n-3][i][0]+1,coin[n-3][i][1]))

    for i in range(0, len(coin[n-5])):
        if (coin[n-5][i][0])*3+(coin[n-5][i][1]+1)*5==n:
            coin_n.add((coin[n-5][i][0],coin[n-5][i][1]+1))

    return list(coin_n)

for i in range(1000):
    coin.append(coin_35(i))
    print(i,sorted(coin[i]))