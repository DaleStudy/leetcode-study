import java.util.*;
class Solution {

    // dfs with memoization => O(N)
    public int rob(int[] nums) {
        Map<Integer,Integer> memo = new HashMap<>();
        return dfs(0, nums, memo);
    }

    public int dfs(int start, int[] nums, Map<Integer, Integer> memo) {
        if (memo.containsKey(start)) return memo.get(start);
        if (start >= nums.length) {
            memo.put(start, 0);
        } else {
            memo.put(start, Math.max(
                    nums[start] + dfs(start + 2, nums, memo),
                    dfs(start + 1, nums, memo))
            );
        }
        return memo.get(start);
    }
}
