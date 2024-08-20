/**
 * @param {number} n
 * @return {number}
 */

/**
 * Runtime: 59ms, Memory: 50.76MB
 *
 * Time complexity: O(logN)
 * -> While
 * Space complexity: O(logN)
 * -> To save binary.split()
 *
 * **/

var hammingWeight = function (n) {
  let binary = "";

  while (n > 1) {
    let left = n % 2;
    binary += left.toString();
    n = Math.floor(n / 2);
  }
  binary = binary + n.toString();

  const count = binary.split("1").length - 1;

  return count;
};
