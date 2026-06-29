/**
 * @param {number} n
 * @return {number}
 */
function climbStairs(n) {
  if (n <= 2) return n;

  let arr = new Array(n + 1);

  arr[0] = 1;
  arr[1] = 2;

  for (let i = 2; i < arr.length; i++) {
    arr[i] = arr[i - 2] + arr[i - 1];
  }

  return arr[n - 1];
}
