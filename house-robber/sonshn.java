/**
 * DFS를 이용한 재귀 풀이
 * 
 * 시간 복잡도: O(2^n), 공간 복잡도: O(n)
 */
class Solution {
    public int rob(int[] nums) {
        return dfs(nums, 0);
    }

    private int dfs(int[] nums, int start) {
        if (start >= nums.length) {
            return 0;
        }

        return Math.max(
            nums[start] + dfs(nums, start + 2),
            dfs(nums, start + 1)
        );
    }
}
