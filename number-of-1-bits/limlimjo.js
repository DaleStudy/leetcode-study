// 시간 복잡도: O(log n)
// 공간 복잡도: O(log n)

/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function (n) {
  let binary = n.toString(2);
  let count = 0;

  for (let i = 0; i < binary.length; i++) {
    if (binary[i] === "1") {
      count += 1;
    }
  }
  return count;
};
