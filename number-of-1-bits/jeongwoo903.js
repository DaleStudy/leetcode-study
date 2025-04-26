/*
* 시간 복잡도: O(log n)
* 공간 복잡도; O(log n)
*/

/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function(n) {
  const dec = n.toString(2);
  const parsedBits = [...dec].filter(item => item === '1');
  return parsedBits.length;
};
