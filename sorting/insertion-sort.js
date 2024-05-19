const unsortedArray = [4, 2, 7, 1, 9, 3];
const sortedArray = insertionSortArray([...unsortedArray]);

console.log("Unsorted array:", unsortedArray);
console.log("Sorted array:", sortedArray);

// WE START FROM 1st Idx
// and our current elem is our i
// start from  elem before current elm
// all about left side comparision and move idx

function insertionSortArray(arr) {
  let n = arr.length;

  for (let i = 1; i < n; i++) {
    let currentElm = arr[i];
    let j = i - 1;

    while (arr[j] >= 0 && arr[j] > currentElm) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = currentElm;
  }

  return arr;
}
