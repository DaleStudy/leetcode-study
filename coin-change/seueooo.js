/**
 * bfs
 * 시간 복잡도: O(amount * n)
 * 공간 복잡도: O(amount)
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function (coins, amount) {
  let q = [];
  let visited = new Set();
  q.push([0, 0]);
  while (q.length) {
    const [sum, count] = q.shift();
    if (sum === amount) return count;
    if (visited.has(sum)) continue;
    visited.add(sum);
    for (let i = 0; i < coins.length; i++) {
      const nextSum = sum + coins[i];
      if (nextSum <= amount) {
        q.push([nextSum, count + 1]);
      }
    }
  }
  return -1;
};
