// dfs를 이용한 풀이
// dp 배열을 이용한 것보다 공간복잡도가 상대적으로 낮게 잡힘 40.4mb -> 40.1mb
// 이유가 뭔지는 조금 더 고민해봐야할 듯
class Solution {
    public int climbStairs(int n) {
        return dfs(n, new HashMap<>());
    }

    private int dfs(int n, Map<Integer, Integer> memo) {
        if (n == 0) {
            return 1;
        }
        if (n < 0) {
            return 0;
        }
        if (memo.containsKey(n)) {
            return memo.get(n);
        }

        int result = dfs(n - 1, memo) + dfs(n - 2, memo);
        memo.put(n, result);

        return result;
    }
}

// 가장 먼저 생각한 풀이
// 피보나치 수열의 형태의 결과물을 갖는다.
// O(N)의 점화식을 세울 수 있으면 어느 방식으로도 풀림
class Solution {
    public int climbStairs(int n) {
        if(n == 1) return 1;
        if(n == 2) return 2;
        
        int[] dp = new int[n + 1];
        dp[1] = 1; // 1
        dp[2] = 2; // 1+1, 2

        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }

        return dp[n];
    }
}
