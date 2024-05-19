(function test() {
  const testArray1 = [4, 5, 2, 1, 3, 8];
  console.log(selectionSort(testArray1));
})();

// WE TAKE THE INDEX /
// WE CHECK IF RIGHT ELEM IS < OUR MIN
// WE SWAP ONLY AFTER LOOP ENDS

function selectionSort(arr) {
  const n = arr.length;
  for (let i = 0; i < n; i++) {
    let minIdx = i;
    for (let j = i + 1; j < n; j++) {
      if (arr[j] < arr[minIdx]) {
        minIdx = j;
      }
    }
    if (minIdx !== i) {
      [arr[minIdx], arr[i]] = [arr[i], arr[minIdx]];
    }
  }

  return arr;
}
