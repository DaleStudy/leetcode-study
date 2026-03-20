/**
 * @param {number} n
 * @return {number}
 */

var climbStairs = function (n) {
  if (n === 1) return 1;
  if (n === 2) return 2;
  const arr = [0, 1, 2];
  let i = 3;
  while (i <= n) {
    const temp = arr[i - 1] + arr[i - 2];
    arr.push(temp);
    i++;
  }

  return arr[n];
};
