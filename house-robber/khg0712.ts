function rob(nums: number[]): number {
    const memo: Record<number, number> = {};
    
    function dfs (start: number): number {
        if(memo[start] != null) {
            return memo[start];
        }

        if(start >= nums.length) {
            return 0;
        }

        memo[start] = Math.max(nums[start] + dfs(start + 2), dfs(start + 1));
        return memo[start];
    }

    return dfs(0);
};
