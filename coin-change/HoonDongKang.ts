/**
 * [Problem]: [322] Coin Change
 *
 * (https://leetcode.com/problems/coin-change/description/)
 */
function coinChange(coins: number[], amount: number): number {
    // 시간복잡도: O(c^a)
    // 공간복잡도: O(a)
    // Time Exceed
    function dfsFunc(coins: number[], amount: number): number {
        if (!amount) return 0;
        let result = dfs(amount);

        return result <= amount ? result : -1;

        function dfs(remain: number): number {
            if (remain === 0) return 0;
            if (remain < 0) return amount + 1;

            let min_count = amount + 1;

            for (let coin of coins) {
                const result = dfs(remain - coin);
                min_count = Math.min(min_count, result + 1);
            }

            return min_count;
        }
    }
    // 시간복잡도: O(ca)
    // 공간복잡도: O(a)
    function dpFunc(coins: number[], amount: number): number {
        const dp = new Array(amount + 1).fill(amount + 1);
        dp[0] = 0;

        for (let coin of coins) {
            for (let i = coin; i <= amount; i++) {
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }

        return dp[amount] <= amount ? dp[amount] : -1;
    }

    // 시간복잡도: O(ca)
    // 공간복잡도: O(a)
    function memoizationFunc(coins: number[], amount: number): number {
        const memo: Record<number, number> = {};

        const result = dfs(amount);
        return result <= amount ? result : -1;

        function dfs(remain: number): number {
            if (remain === 0) return 0;
            if (remain < 0) return amount + 1;
            if (remain in memo) return memo[remain];

            let min_count = amount + 1;

            for (let coin of coins) {
                const res = dfs(remain - coin);
                min_count = Math.min(min_count, res + 1);
            }

            memo[remain] = min_count;

            return min_count;
        }
    }

    return memoizationFunc(coins, amount);
}
