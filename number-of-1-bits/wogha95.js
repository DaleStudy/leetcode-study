// TC: O(log n)
// SC: O(1)

/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function (n) {
  return n
    .toString(2)
    .split("")
    .filter((s) => s === "1").length;
};
