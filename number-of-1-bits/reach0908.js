/**
 * 시간복잡도: O(n)
 * 공간복잡도: O(1)
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function (n) {
  let num = n;

  let count = 0;

  while (num > 0) {
    const left = num % 2;

    if (left === 1) {
      count += 1;
    }

    num = Math.floor(num / 2);
  }

  return count;
};
