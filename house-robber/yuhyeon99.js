/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    const memo = {};

    function dfs(start) {
        if(memo[start] !== undefined) return memo[start];
        if(start >= nums.length) {
            memo[start] = 0;
        } else {
            memo[start] = Math.max(nums[start] + dfs(start + 2), dfs(start + 1))
        }
        return memo[start];
    }

    return dfs(0);
};
