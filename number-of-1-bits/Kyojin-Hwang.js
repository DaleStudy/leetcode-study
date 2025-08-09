/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function (n) {
  return n
    .toString(2)
    .split("")
    .filter((bit) => bit === "1").length;
};
