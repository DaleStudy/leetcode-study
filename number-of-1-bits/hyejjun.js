/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function (n) {

  let val = n.toString(2);

  let res = 0;
  [...val].forEach((val) => res += parseInt(val))

  return res;

};

// O(LogN)

console.log(hammingWeight(11));
console.log(hammingWeight(128));
console.log(hammingWeight(2147483645));
