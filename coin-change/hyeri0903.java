class Solution {
    int minLen = Integer.MAX_VALUE;
    public int coinChange(int[] coins, int amount) {
        /**
        1.문제: amount 를 만족시킬 수 있는 가장 적은 수의 coins
        2.조건
        - 모두 다른 값 integer로 구성된 배열
        - amount 를 만들 수 없는 경우 -1 return
        - coins.length 최소 1, 최대 12
        - 원소값 최소 = 1
        - amount 최소 = 0
        3.풀이
        - amount 를 만족시키는 최소 조합 길이를 구한다. dfs? -> TLE
        - dp
         */

        int n = coins.length;
        //최대 코인개수 = amount
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;

        for(int i = 1; i <= amount; i++) {
            for(int coin : coins) {
                //코인 사용가능한 경우
                if(i - coin >= 0) {
                    dp[i] = Math.min(dp[i], dp[i-coin] + 1);
                }
            }
        }
        //amount 못만든 경우
        if(dp[amount] > amount) {
            return -1;
        }
        return dp[amount];

        // if(n != 0 && amount == 0) return 0;
        // Arrays.sort(coins);
        // dfs(n - 1, 0, coins, amount, 0);
        // if(minLen == Integer.MAX_VALUE) {
        //     return -1;
        // }
        //return minLen;
    }

    void dfs(int index, int total, int[] coins, int amount, int count) {
        if(total > amount) return;

        if(total == amount) {
            minLen = Math.min(minLen, count);
            return;
        }

        if(count >= minLen) return;

        for(int i = index; i >=0; i--) {
            dfs(i, total + coins[i], coins, amount, count+1);
        }
    }
}
