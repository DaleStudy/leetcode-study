class Solution {
    /*
    time complexity: O(amount × n)
    space complexity: O(amount)
    */
    public int coinChange(int[] coins, int amount) {
        int[] memo = new int[amount + 1];
        Arrays.fill(memo, amount + 1); // 초기값: 만들 수 없는 큰 수
        memo[0] = 0; // 0원을 만들기 위한 동전 수는 0개

        for (int coin : coins) {
            for (int i = coin; i <= amount; i++) {
                memo[i] = Math.min(memo[i], memo[i - coin] + 1);
            }
        }

        return memo[amount] > amount ? -1 : memo[amount];
    }
}
