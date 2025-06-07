function canJump(nums: number[]): boolean {
    const memo: boolean[] = new Array(nums.length).fill(null)
    const dfs = (start: number): boolean => {
        if (start >= nums.length - 1) {
            return true
        }
        if (memo[start] != null) return memo[start]
        const maxJump = nums[start]
        for (let i = 1; i <= maxJump; i++) {
            if (dfs(start + i)) {
                memo[start] = true
                return true
            }
        }
        memo[start] = false
        return false
    }
    return dfs(0)
};
