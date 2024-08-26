var countBits = function (n) {
  let result = [];
  for (let i = 0; i <= n; i++) {
    result.push(countOneBits(i));  // count one bits for each i until n
  }

  function countOneBits(num) { // method to count one bits
    let oneBitCount = 0;
    while (num) {
      oneBitCount += num % 2;
      num = num >> 1;
    }
    return oneBitCount;
  }

  return result;
};

// test cases
console.log(countBits(2)); // [0,1,1]
console.log(countBits(5)); // [0,1,1,2,1,2]

// time - O(nlogn) 
// space - O(n)
