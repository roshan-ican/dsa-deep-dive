// function fibo(n) {
//     if (n <= 2) return 1;
//     return fibo(n - 1) + fibo(n - 2)
// }

// function printFibonacciSequence(n) {
//     for (let i = 1; i <= n; i++) {
//         console.log(`Fibonacci(${i}):`, fibo(i));
//     }
// }


function memoizedFibo() {
    const cache = {}
    function fibo(n) {
        if (n <= 2) return 1;
        if (cache[n]) return cache[n]

        cache[n] = fibo(n - 1) + fibo(n - 2)
        return fibo(n - 1) + fibo(n - 2)
    }
    return fibo
}
const fibo = memoizedFibo();

function printFibonacciSequence(n) {
    for (let i = 1; i <= n; i++) {
        console.log(`Fibonacci(${i}):`, fibo(i));
    }
}

// Example: Print Fibonacci sequence up to the 20th number
printFibonacciSequence(100);