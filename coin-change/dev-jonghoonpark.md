- 문제: https://leetcode.com/problems/coin-change/
- 풀이: https://algorithm.jonghoonpark.com/2024/02/26/leetcode-322

## dfs로 풀기

```java
class Solution {
    public int coinChange(int[] coins, int amount) {
        if(amount == 0) {
            return 0;
        }

        int[] dp = new int[amount + 1];

        List<Integer> sortedCoins = Arrays.stream(coins).boxed()
                .sorted(Collections.reverseOrder())
                .toList();

        sortedCoins.forEach(coin -> dfs(dp, sortedCoins, amount, coin));

        return dp[0] == 0 ? -1 : dp[0];
    }

    void dfs(int[] dp, List<Integer> coins, int amount, int selectedCoin) {
        int currentPointer = amount - selectedCoin;
        if (currentPointer < 0) {
            return;
        }

        if (dp[currentPointer] == 0 || dp[currentPointer] > dp[amount] + 1) {
            dp[currentPointer] = dp[amount] + 1;
            coins.forEach(coin -> dfs(dp, coins, currentPointer, coin));
        }
    }
}
```

### TS, SC

코인의 수를 n 이라고 했을 때, `O(n * amount ^ 2)` 의 시간복잡도와 `O(amount)` 의 공간복잡도를 가진다.

## dp로 풀기

```java
public class Solution {
    public int coinChange(int[] coins, int amount) {
        int max = amount + 1;
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, max);
        dp[0] = 0;

        for (int i = 1; i <= amount; i++) {
            for (int j = 0; j < coins.length; j++) {
                if (coins[j] <= i) {
                    dp[i] = Math.min(dp[i], dp[i - coins[j]] + 1);
                }
            }
        }

        return dp[amount] > amount ? -1 : dp[amount];
    }
}
```

### TS, SC

코인의 수를 n 이라고 했을 때, `O(n * amount)` 의 시간복잡도와 `O(amount)` 의 공간복잡도를 가진다.
