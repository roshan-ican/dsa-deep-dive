function collectOdd(arr) {
  let result = [];

  function helper(helperInput) {
    if (helperInput.length === 0) {
      return;
    }
    if (helperInput[0] % 2 !== 0) {
      result.push(helperInput[0]);
    }
    helper(helperInput.slice(1));
  }
  helper(arr);
  return result;
}

console.log(collectOdd([1, 2, 3, 4, 5, 6, 7]));

function collectOddConcat(arr) {
  let newArr = [];

  if (arr.length === 0) {
    return newArr;
  }
  if (arr[0] % 2 !== 0) {
    newArr.push(arr[0]);
  }
  newArr = newArr.concat(collectOddConcat(arr.slice(1)));
  return newArr;
}
console.log(collectOddConcat([1, 2, 3, 4, 11, 15, 13], [1, 2, 3, 4, 5, 6, 7]));
console.log(Math.pow(10, 3), "_pow");

function factorial(n) {
  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(5), "__factorial");
