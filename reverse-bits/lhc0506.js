/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function(n) {
  return parseInt(n.toString(2).padStart(32, '0').split('').reverse().join(''), 2);
};

// 시간복잡도: O(n)
// 공간복잡도: O(1)
