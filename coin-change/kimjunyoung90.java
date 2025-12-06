import java.util.Arrays;

class Solution {
    //풀이 원리 = 특정 금액을 만들 때 최소 동전 수는 몇 개?
    //예) 0원은 동전 0개
    // 1원은 동전 1개
    // 2원은 동전 1
    public int coinChange(int[] coins, int amount) {
        //불가능한 값
        int max = amount + 1;
        int[] dp = new int[amount + 1];
        //최소 동전 수를 모두 불가능한 값으로 설정
        Arrays.fill(dp, max);
        dp[0] = 0;

        //금액 1원 부터 계산
        for (int i = 1; i <= amount; i++) {
            //사용할 수 있는 동전을 꺼냄
            for(int coin: coins) {
                if (coin <= i) {
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }

        return dp[amount] > amount ? -1 : dp[amount];
    }
}
