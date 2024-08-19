var hammingWeight = function (n) {
  let bitVal = n.toString(2); // convert input value to bit
  let setBits = 0;
  for (const char of bitVal) { // iterate through the string bit value to check the number of "1"s
    if (char === "1") setBits++; // increment if char === "1"
  }
  return setBits;
};

// test cases
console.log(hammingWeight(11)); // 3
console.log(hammingWeight(128)); // 1
console.log(hammingWeight(2147483645)); // 30

// space - O(1) - created only constant variables
// time - O(n) - iterate through the bitVal string (larger the number the longer the string)
