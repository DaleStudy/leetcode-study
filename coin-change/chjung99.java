class Solution {
    public int coinChange(int[] coins, int amount) {
        int n = coins.length;
        TreeSet<Integer> set = new TreeSet<>();
        int[] dp = new int[amount+1];

        for (int coin: coins) {
            if (coin > amount) continue;
            set.add(coin);
            dp[coin] = 1;
        }
        // System.out.println("======");
        for (int i = 1; i <= amount; i++) {
            int minKey = -1;
            int minValue = -1;
            for (int key: set) {
                if (i - key < 0 || dp[i-key] == -1) continue;
                if (minKey == -1) {
                    minKey = key;
                    minValue = 1 + dp[i - key];
                }
                else if (minValue > 1 + dp[i-key]){
                    minKey = key;
                    minValue = 1 + dp[i - key];
                }
            }
            dp[i] = minValue;
        }
        // System.out.println("======");
        // for (int i = 0; i <= amount; i++) {
        //     System.out.print(dp[i]+", ");
        // }
        return dp[amount];
    }
}

