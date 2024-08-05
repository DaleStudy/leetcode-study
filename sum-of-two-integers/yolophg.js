// Time Complexity: O(log max(a, b))
// Space Complexity: O(log max(a, b))

var getSum = function (a, b) {
  // if there is no carry, return a as the result
  if (b === 0) return a;

  // calculate the sum without carry using XOR
  let sum = a ^ b;

  // calculate the carry using AND and left shift
  let carry = (a & b) << 1;

  // recursively call getSum with sum and carry
  return getSum(sum, carry);
};
