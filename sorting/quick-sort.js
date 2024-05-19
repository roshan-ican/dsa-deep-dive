// [4, 8, 2, 1, 5, 7, 6, 3]
// //PIVOT
// [4, 8, 2, 1, 5, 7, 6, 3]
// //pivot[0] > arr[i]

// [4, 2, 8, 1, 5, 7, 6, 3]
// [4, 2, 1, 8, 5, 7, 6, 3]
// [3, 2, 1, 4, 8, 5, 7, 6]
// [3, 2, 1]   [8, 5, 7, 6]
// // INDEX ONLY NOT VALUE
console.log(quickSort([4, 8, 2, 1, 5, 7, 6, 3, -1]));

function pivot(arr, start = 0, end = arr.length - 1) {
  //finds the correct position of pivot
  let pivot = arr[start];
  let swapIdx = start;
  const swap = (arr, idx1, idx2) => {
    [arr[idx1], arr[idx2]] = [arr[idx2], arr[idx1]];
  };

  for (let i = start + 1; i <= end; i++) {
    if (pivot > arr[i]) {
      swapIdx++;
      swap(arr, swapIdx, i);
    }
  }
  swap(arr, start, swapIdx);
  return swapIdx;
}

function quickSort(arr, left = 0, right = arr.length - 1) {
  if (left < right) {
    const pivotIdx = pivot(arr, left, right);
    quickSort(arr, left, pivotIdx - 1); // finds the pivot in left sub array
    quickSort(arr, pivotIdx + 1, right); // right
  }
  return arr;
}
