function recursiveFib(num) {
  if (num === 0 || num === 1) {
    return 1;
  }
  return recursiveFib(num - 1) + recursiveFib(num - 2);
}

console.log(recursiveFib(5));