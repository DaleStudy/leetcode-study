/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */

// Time Complexity: O(log(max(a, b)))
// Space Complexity: O(1)

var getSum = function (a, b) {
  // XOR (^): outputs true (or 1) if the inputs are different, and false (or 0) if the inputs are the same.
  // And (&): compares each bit of two numbers and returns 1 only if both bits are 1; otherwise, it returns 0.
  // left shitf (<<): moves the bits one position to the left, which is the same as multiplying by 2.

  while (b !== 0) {
    let carry = (a & b) << 1;
    a = a ^ b;
    b = carry;
  }

  return a;
};

