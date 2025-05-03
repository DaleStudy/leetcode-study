/**
[문제풀이]
- 배열에 주어진 수를 더해서 amount 만들기
- 배열은 중복 가능
- amount를 만들 수 없으면 -1
- amount를 만든 동전의 최소 개수 구하기
- DP
time: O(N M), space: O(N)

[회고]
DP로 풀면 되지 않을까 라는 짐작은 가는데,
아직 풀이방법이 부족하다..
해결방법을 보고 겨우 이해는 했다..
 */
class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;

        for (int coin : coins) {
            for (int i = coin; i <= amount; i++) {
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }
}

