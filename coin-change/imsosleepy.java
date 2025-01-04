// 비슷한 문제를 푼 적이 있어서 쉽게 해결
// https://www.acmicpc.net/problem/2294
// O(N * amount) 시간복잡도가 배열 크기와 amount에 종속된다.
// dp[N]만 사용하므로 공간복잡도는 O(N)
class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1); 불가능한 큰 값
        dp[0] = 0;

        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (i >= coin) {
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }

        return dp[amount] > amount ? -1 : dp[amount];
    }
}
