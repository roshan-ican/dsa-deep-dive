var isSquare = function (n) {
  const negative = " Negative numbers cannot be square numbers";
  if (n < 0) return false ;
  if(n === 0) return true;
  const squareRoot = Math.sqrt(n)
  if (squareRoot === Math.floor(squareRoot)) {
    return true;
  } else {
    return false;
  }
};
console.log(isSquare(25), "res")