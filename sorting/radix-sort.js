// // TO GET THE BASE ELEMENT
// function getDigit(num, i) {
//   return Math.floor(Math.abs(num) / Math.pow(10, i)) % 10;
// }
// // TO COUNT THE NUMBER IN THE ARRAY
// function digitCount(num) {
//   if (num === 0) return 1;
//   return Math.floor(Math.log10(Math.abs(num))) + 1;
// }
// // MAX NUM OF DIGITS
// function mostDigits(nums) {
//   let maxDigits = 0;
//   for (let i = 0; i < nums.length; i++) {
//     maxDigits = Math.max(maxDigits, digitCount(nums[i]));
//   }
//   return maxDigits;
// }
// function radixSort(nums) {
//   let mostDigitsCount = mostDigits(nums);
//   for (let k = 0; k < mostDigitsCount; k++) {
//     let digitBuckets = Array.from({ length: 10 }, () => []);
//     for (let i = 0; i < nums.length; i++) {
//       //   let getDigits = getDigit(nums[i], k);
//       // THE UGLY WAY TO PUT NUMS INTO THEIR BUCKETS
//       let digit = getDigit(nums[i], k);
//       digitBuckets[digit].push(nums[i]);
//     }
//     // console.log(...digitBuckets);
//     nums = [].concat(...digitBuckets);
//   }
//   return nums;
// }
console.log(radixSort([2443, 323342, 2411, 876, 78, 1, 2, 5, 6, 9]));

// HELPER FUNCTION getDigit()
function getDigits(nums, place) {
  return Math.floor(Math.abs(nums) / Math.pow(10, place)) % 10;
}
console.log(getDigits(43263, 0)); // 3
// HELPER FUNCTION digitCount()
function digitCount(num) {
  if (num === 0) return 1;
  return Math.floor(Math.log10(Math.abs(num))) + 1;
}

console.log(digitCount(3547));
// HELPER FUNCTION max digit()
function mostDigit(nums) {
  let max = 0;
  for (let i = 0; i < nums.length; i++) {
    max = Math.max(max, digitCount(nums[i]));
  }
  return max;
}
console.log(mostDigit([44, 849, 1, 3333]));
// MAIN RADIX SORT
function radixSort(arrOfNums) {
  let mostNoOfDigit = mostDigit(arrOfNums);
  for (let k = 0; k < mostNoOfDigit; k++) {
    let buckets = Array.from({ length: 10 }, () => []);
    for (let i = 0; i < arrOfNums.length; i++) {
      let digit = getDigits(arrOfNums[i], k);
      buckets[digit].push(arrOfNums[i]);
    }
    arrOfNums = [].concat(...buckets);
  }
  return arrOfNums;
}
