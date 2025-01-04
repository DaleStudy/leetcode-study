/*
input : array of integers each element represents coins, single integer amount
output : fewest number of coin to make up the amount
constraint
1) elements are positive?
yes
2) coins are in integer range?
yes
3) range of amoutn
integer range?
[0, 10^4]
4) at least one valid answer exists?
nope. if there no exist than return -1

edge. case
1) if amount == 0 return 0;

 solution 1) top-down approach

amount - each coin
    until amount == 0
    return min
tc : O(n * k) when n is amount, k is unique coin numbers
sc : O(n) call stack

solution 2) bottom-up
tc : O(n*k)
sc : O(n)
let dp[i] the minimum number of coins to make up amount i

 */
class Solution {
  public int coinChange(int[] coins, int amount) {
    //edge
    if(amount == 0) return 0;
    int[] dp = new int[amount+1];
    dp[0] = 0;
    for(int i = 1; i<= amount; i++) {
      dp[i] = amount+1;
      for(int coin: coins) {
        if(i - coin >= 0) {
          dp[i] = Math.min(dp[i], dp[i-coin] + 1);
        }
      }
    }
    return dp[amount] == amount+1 ? -1 : dp[amount];
  }
}
