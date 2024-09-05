const coinChange = function (coins, target) {
  const dp = new Array(target + 1).fill(target + 1);

  dp[0] = 0;
  for (let i = 1; i <= target; i++) {
    for (let j = 0; j < coins.length; j++) {
      if (i >= coins[j]) {
        dp[i] = Math.min(dp[i], 1 + dp[i - coins[j]]);
      }
    }
  }
  return dp[target] === target + 1 ? -1 : dp[target];
};

console.log(coinChange([1, 2, 5], 11)); //3
console.log(coinChange([2], 3)); //-1
console.log(coinChange([1], 0)); //0

console.log(coinChange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 40)); //4

console.log(coinChange([186, 419, 83, 408], 6249)); //20

console.log(
  coinChange([411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422], 9864)
); //24

console.log(coinChange([1, 2], 3)); //2
