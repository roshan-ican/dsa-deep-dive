(function test() {
  const testArray1 = [4, 5, 2, 1, 3, 8];
  console.log(mergeSort(testArray1));
})();

//Math.floor
//slice
//shift
//push
//concat

// function mergeSort(arr) {
//   const n = arr.length;
//   if (n <= 1) {
//     return arr;
//   }
//   const mid = Math.floor(n / 2);
//   const left = arr.slice(0, mid);
//   const right = arr.slice(mid);

//   return merge(mergeSort(left), mergeSort(right));
// }
// function merge(left, right) {
//   const result = [];
//   while (left.length && right.length) {
//     if (left[0] < right[0]) {
//       result.push(left.shift());
//     } else {
//       result.push(right.shift());
//     }
//   }
//   return result.concat(left.slice()).concat(right.slice());
// }

function mergeSort(arr) {
  const n = arr.length;
  if (n <= 1) {
    return arr;
  }
  const mid = Math.floor(n / 2);
  const left = arr.slice(0, mid);
  const right = arr.slice(mid);
  return merge(mergeSort(left), mergeSort(right));
}

function merge(left, right) {
  const result = [];
  while (left.length && right.length) {
    if (left[0] < right[0]) {
      result.push(left.shift());
    } else {
      result.push(right.shift());
    }
  }
  return result.concat(left.slice()).concat(right.slice());
}
