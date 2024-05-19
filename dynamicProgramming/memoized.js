function fib(n, memo = []) {
    if (memo[n] !== undefined) return memo[n]
    if (n <= 2) return 1;
    var res = fib(n - 1, memo) + fib(n - 2, memo)
    console.log(res)
    return res
}

// fib(33)

function fib_table(n) {
    if (n <= 2) return 1
    var fibNums = [0, 1, 1]
    for (var i = 3; i <= n; i++) {
        fibNums[i] = fibNums[i - 1] + fibNums[i - 2]
    }
    console.log(fibNums[n]);
    return fibNums[n]
}
fib_table(10000)