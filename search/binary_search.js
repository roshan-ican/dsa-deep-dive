// Original Solution
function binarySearch(arr, elem) {
  var start = 0;
  var end = arr.length - 1;
  var middle = Math.floor((start + end) / 2);
  while (arr[middle] !== elem && start <= end) {
    if (elem < arr[middle]) {
      end = middle - 1;
    } else {
      start = middle + 1;
    }
    middle = Math.floor((start + end) / 2);
  }
  if (arr[middle] === elem) {
    return middle;
  }
  return -1;
}

// Refactored Version
function binarySearch(arr, elem) {
  var start = 0;
  var end = arr.length - 1;
  var middle = Math.floor((start + end) / 2);
  while (arr[middle] !== elem && start <= end) {
    if (elem < arr[middle]) end = middle - 1;
    else start = middle + 1;
    middle = Math.floor((start + end) / 2);
  }
  return arr[middle] === elem ? middle : -1;
}
// console.log(binarySearch([2, 5, 6, 9, 13, 15, 28, 30], 15));

function myBinarySearch(arr, elem) {
    let left = 0 
    let right = arr.length - 1;
    let mid = Math.floor((left + right) / 2)
    while(arr[mid] !== elem && left <= right){
        if(arr[mid] > elem){
            right = mid + 1
        } else {
            left = mid -1
        }
        mid = Math.floor((left + right) / 2)
    }
    return arr[mid] === elem ? mid : -1

}

console.log(myBinarySearch([2, 5, 6, 9, 13, 15, 28, 30], 15));
