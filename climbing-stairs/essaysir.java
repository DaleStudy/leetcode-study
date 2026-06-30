import java.util.*;

class Solution {
    // TC: O(2의 N승)
    // SC: O(N)
    public static Map<Integer, Integer> memo = new HashMap<>();

    public int climbStairs(int n) {
        // 1과 2로만 움직일 수 있을 때, 도달할 수 있는 모든 방법의 수에 대해 구하시오
        // DPS (QUEUE)  , BPS (STACK)
        return dfs(n);
    }

    // dfs(5) -> dfs(3) + dfs(4) -> dfs(2) + dfs(1) + dfs(3) + dfs(2)
    public static int dfs(int n){
        if ( n == 1) return 1;
        if ( n == 2) return 2;
        if ( memo.containsKey(n) ) return memo.get(n);

        int result = dfs(n-1) + dfs(n-2);
        memo.put(n, result);
        return result;
    }
}
