function reverseStr(str) {
  if (str.length < 2) {
    return str;
  }
  return reverseStr(str.slice(1, str.length)) + str[0];
}
console.log(reverseStr("Roshan"), "____reversedStr");
