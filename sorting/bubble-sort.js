const unsortedArray = [4, 2, 7, 1, 9, 3];

(function test() {
  const sortedArray = bubbleSort(unsortedArray.slice());

  console.log("Unsorted array:", unsortedArray);
  console.log("Sorted array:", sortedArray);
  console.log("test");
})();
function bubbleSort(arr) {
  let swapped;
  do {
    swapped = false;
    for (let i = 0; i < arr.length ; i++) {
      if (arr[i+1] && arr[i] > arr[i + 1]) {
        [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]]
        swapped = true
      }
    }
  } while (swapped);
  return arr; 
}
