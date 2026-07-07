import java.util.*;

// TC: O(n)
// SC: O(n)
class Solution {
    static int[] memo = new int[46];


    public int climbStairs(int n) {

        if (n == 1) return 1;
        if (n == 2) return 2;
        memo[1] = 1;
        memo[2] = 2;

        dfs(n);
        return memo[n];
    }

    private int dfs(int num) {

        //이미 계산한적이 있으면
        if (memo[num] != 0) {
            return memo[num];
        }

        memo[num] = dfs(num - 1) + dfs(num - 2);
        return memo[num];

    }
}
