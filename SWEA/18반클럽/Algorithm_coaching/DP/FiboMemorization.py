def fibo_memo(n, memo=None):
    if memo is None:
        memo = {}
        
    if n in memo:
        print(memo, n, '@', memo[n])
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibo_memo(n-1, memo) + fibo_memo(n-2, memo)
    return memo[n]

print(fibo_memo(10))