/*
    Problem: https://leetcode.com/problems/coin-change/
    Description: return the fewest number of coins that you need to make up that amount
    Concept: Array, Dynamic Programming, Breadth-First Search
    Time Complexity: O(N²), Runtime 15ms   - N is the amount
    Space Complexity: O(N), Memory 44.28MB
*/
class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount+1];
        Arrays.fill(dp, amount+1);
        dp[0]=0;

        for(int i=1; i<=amount; i++){
            for(int coin : coins){
                if(i >= coin) {
                    dp[i] = Math.min(dp[i], dp[i-coin] +1);
                }
            }
        }
        return dp[amount]>amount? -1: dp[amount];
    }
}
