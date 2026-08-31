def fib(n):
    cache = {}
    
    def fib_cache(n):
        if n in cache:
            return cache[n]
        if n < 2:
            result = n
        else:
            result = fib_cache(n - 1) + fib_cache(n - 2)
            
        cache[n] = result
        return result
    return fib_cache(n)

print(fib(6))