/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */

/**
 * combination sum 풀이를 활용했지만 amount가 커서
 * time limit exceeded
 * */

var coinChange = function (coins, amount) {
  let answer = [];
  let coins_desc = coins.reverse();

  if (amount === 0) return 0;

  function permute(arr = [], sum = 0, index = 0) {
    if (sum > amount) return;
    // 같은 경우에만 result에 담기
    if (sum === amount) {
      if (answer.length === 0) {
        answer = [...arr];
      } else {
        if (arr.length < answer.length) {
          answer = [...arr];
        } else {
          return answer.length;
        }
      }
    }
    for (let i = index; i < coins.length; i++) {
      // target보다 합이 작으면 재귀적으로 해당 값을 arr에 넣고, sum에 추가
      permute([...arr, coins_desc[i]], sum + coins_desc[i], i);
    }
  }
  permute();
  return answer.length === 0 ? -1 : answer.length;
};

/**
 * 풀이(참고): combination sum을 dp로 풀려고 했었는데, 사실 이 문제가 dp로 풀어야 하는 문제
 */

/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function (coins, amount) {
  let dp = Array.from({ length: amount + 1 }, () => Infinity);
  dp[0] = 0;

  for (const coin of coins) {
    for (let i = coin; i <= amount; i += 1) {
      dp[i] = Math.min(dp[i], dp[i - coin] + 1);
    }
  }

  return dp[amount] === Infinity ? -1 : dp[amount];
};
