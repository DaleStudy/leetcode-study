import java.util.Arrays;

class Solution {
    // TC: O(amount * coins.length)
    // SC: O(amount)
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        // Maximum depth = amount
        // amount + 1 means undefined; set to use Math.min
        Arrays.fill(dp, amount + 1);

        dp[0] = 0;

        for(int i = 1; i <= amount; i++){
            for(int coin : coins){
                if(i - coin >= 0){
                    // depth without the coin + with the coin(1)
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }

        return dp[amount] > amount ? -1 : dp[amount];
    }
}

// DFS + Memoization
// class Solution {
//     public int coinChange(int[] coins, int amount) {
//         int[] memo = new int[amount + 1];
//         Arrays.fill(memo, -2); // -2 = 아직 계산 안함
//         return dfs(0, coins, amount, memo);
//     }

//     private int dfs(int depth, int[] coins, int amount, int[] memo){
//         if(amount < 0){
//             return -1;
//         }
//         if(amount == 0){
//             return depth;
//         }

//         if(memo[amount] != -2) return memo[amount];

//         int min = -1;
//         for(int i = 0; i < coins.length; i++){
//             int descended = coins[coins.length - i - 1];
//             int d = dfs(depth + 1, coins, amount - descended, memo);
//             if(d >= 0 && (d < min || min == -1)){
//                 min = d;
//             }
//         }

//         if(memo[amount] == -2) memo[amount] = min; // 계산한 적 없는 경우에만 저장
//         return min;
//     }
// }

// BFS : 문제 서술과 가장 어울리는 풀이지만, Bottom-Up DP가 더 빠른 결과.
// class Solution {
//     public int coinChange(int[] coins, int amount) {
//         Queue<Integer> queue = new LinkedList<>();
//         boolean[] visited = new boolean[amount + 1];

//         queue.offer(amount);
//         visited[amount] = true;

//         int level = 0;

//         while (!queue.isEmpty()) {
//             int size = queue.size();

//             for (int i = 0; i < size; i++) {
//                 int cur = queue.poll();

//                 if (cur == 0) return level;

//                 for (int coin : coins) {
//                     int next = cur - coin;

//                     if (next >= 0 && !visited[next]) {
//                         visited[next] = true;
//                         queue.offer(next);
//                     }
//                 }
//             }

//             level++;
//         }

//         return -1;
//     }
// }
