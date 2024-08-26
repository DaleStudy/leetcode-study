/**
 * @description
 * time complexity: O(n log n)
 * space complexity: O(N)
 *
 * brainstorming:
 * convert integer to bit
 * for loop
 *
 * strategy:
 * string change to hash table
 */
var countBits = function (n) {
  return Array.from({ length: n + 1 }, (_, i) => convertBitCount(i));
};

const convertBitCount = (n) => {
  let count = 0;
  while (n > 0) {
    count += n % 2;
    n = Math.floor(n / 2);
  }
  return count;
};
