/**
 * @param {number} n
 * @return {number}
 */

// week3 다시 올림
var hammingWeight = function (n) {
  const binary = n.toString(2);
  const arr = [...binary];
  let count = 0;
  arr.map((num) => {
    if (num === "1") {
      count++;
    }
  });
  return count;
};
