/**
 * [Problem]: [213] House Robber II
 * (https://leetcode.com/problems/house-robber-ii/description/)
 */
function rob(nums: number[]): number {
    //시간복잡도 O(n)
    //공간복잡도 O(n)
    function memoizationFunc(nums: number[]): number {
        const memo = new Map<string, number>();
        const length = nums.length;

        function dfs(idx: number, first = false) {
            const key = `${idx}_${first}`;
            if (memo.has(key)) return memo.get(key)!;

            if (idx === length - 1) return first ? 0 : nums[idx];
            if (idx >= length) return 0;
            if (idx === 0) {
                const result = Math.max(nums[0] + dfs(2, true), dfs(1, false));
                memo.set(key, result);
                return result;
            }

            const result = Math.max(nums[idx] + dfs(idx + 2, first), dfs(idx + 1, first));
            memo.set(key, result);
            return result;
        }

        return dfs(0);
    }

    //시간복잡도 O(n)
    //공간복잡도 O(1)
    function dpFunc(nums: number[]): number {
        if (nums.length === 1) return nums[0];

        function dp(start: number, end: number) {
            let prev = 0;
            let cur = 0;

            for (let i = start; i < end; i++) {
                [prev, cur] = [cur, Math.max(prev + nums[i], cur)];
            }

            return cur;
        }

        return Math.max(dp(0, nums.length - 1), dp(1, nums.length));
    }
}
