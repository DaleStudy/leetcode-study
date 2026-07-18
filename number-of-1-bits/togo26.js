/**
 * @param {number} n
 * @return {number}
 */

// 31 비트 범위는 상수로 취급

// Log-based calculation
// TC: O(1)  / SC: O(1)
// 비트 제약이 없을 경우 -> TC: O(logn) / SC: O(logn)
var hammingWeight = function (n) {
  const BIT_RANGE = 31;
  let bits = Array.from({ length: BIT_RANGE }).fill(0);

  let remainder = n;
  while (remainder > 0) {
    const exp = Math.min(Math.floor(Math.log2(remainder)), BIT_RANGE - 1);
    bits[exp] = true;
    const value = remainder <= 1 ? 1 : Math.pow(2, exp);
    remainder -= value;
  }

  return bits.filter(value => value).length;
};

// Log-based calculation without an array
// TC: O(1) / SC: O(1)
// 비트 제약이 없을 경우 -> TC: O(logn) / SC: O(1)
var hammingWeight = function (n) {
  const BIT_RANGE = 31;
  let bitCount = 0;

  let remainder = n;
  while (remainder > 0) {
    const exp = Math.min(Math.floor(Math.log2(remainder)), BIT_RANGE - 1);
    const value = remainder <= 1 ? 1 : Math.pow(2, exp);
    remainder -= value;
    bitCount++;
  }

  return bitCount;
};

// Converting binary string with the JS feature
// TC: O(1) / SC: O(1)
// 비트 제약이 없을 경우 -> TC: O(logn) / SC: O(logn)
var hammingWeight = function (n) {
  const binaryString = n.toString(2);
  return [...binaryString].filter(v => v === '1').length;
};

// Bit manipulation
// TC: O(1) / SC: O(1)
// 비트 제약이 없을 경우 -> TC: O(logn) / SC: O(logn)
var hammingWeight = function (n) {
  let count = 0;

  while (n > 0) {
    n = n & (n - 1);
    count++;
  }

  return count;
};
