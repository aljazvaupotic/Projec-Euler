#possible
def count(S, m, n ): 
    if (n == 0): 
        return 1
    if (n < 0): 
        return 0
    if (m <=0 and n >= 1): 
        return 0
    return count( S, m - 1, n ) + count( S, m, n-S[m-1] ); 

coins =[1,2,5,10,20,50,100,200]
m = len(coins)
target = 200

print(count(coins,m,target))