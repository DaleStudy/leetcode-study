class Solution {
    private Integer[] memo;

    public int helper(int[] coins, int remain) {
        if (remain < 0) { // 0 이하로 가는 경우 -1로 지정
            return -1;
        }
        if (remain == 0) { // 처음 값은 0으로 설정
            return 0;
        }

        if (memo[remain] != null) {
            return memo[remain];
        }

        int minNumCoin = Integer.MAX_VALUE; // 세개 중에 최소값을 고르는 로직

        for (int coin : coins) {
            int numCoin = helper(coins, remain - coin);
            if (numCoin != -1) { // 도달 가능한 경우
                minNumCoin = Math.min(minNumCoin, numCoin + 1);
            }
        }
        if (minNumCoin < Integer.MAX_VALUE) { // 도달 가능한 경우
            memo[remain] = minNumCoin;
        } else {
            memo[remain] = -1;
        }

        return memo[remain];
    }

    public int coinChange(int[] coins, int amount) {
        memo = new Integer[amount + 1];
        return helper(coins, amount);
    }
}
