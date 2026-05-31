class Solution {
    public boolean canJump(int[] nums) {
        boolean[] visited= new boolean[nums.length];
        dfs(visited, nums, 0);
        return visited[nums.length - 1];
    }
    public void dfs(boolean[] visited, int[] nums, int target) {
        if(visited[nums.length -1]) {
            return;
        }
        if(visited[target]) {
            return;
        }

        visited[target] = true;

        int maxDist = nums[target];
        for(int i = maxDist; i > 0; i--) {
            int nextIdx = target + i;
            if(nextIdx > nums.length - 1) {
                continue;
            }

            dfs(visited, nums, nextIdx);
        }
    }
}
