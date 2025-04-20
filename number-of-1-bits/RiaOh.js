/**
 * @param {number} n
 * @return {number}
 */
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
