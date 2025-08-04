/**
 * [Problem]: [55] Jump Game
 * (https://leetcode.com/problems/jump-game/description/)
 */
function canJump(nums: number[]): boolean {
    // 시간복잡도 O(N^N)
    // 공간복잡도 O(N)
    // Time Limit Exceeded
    function dfsFunc(nums: number[]): boolean {
        function dfs(start: number): boolean {
            if (start === nums.length - 1) return true;
            for (let i = 1; i <= nums[start]; i++) {
                if (dfs(start + i)) return true;
            }
            return false;
        }
        return dfs(0);
    }
    // 시간복잡도 O(N^2)
    // 공간복잡도 O(N)
    function dpFunc(nums: number[]): boolean {
        const n = nums.length;
        const dp = Array(n).fill(false);
        dp[0] = true;

        for (let i = 1; i < n; i++) {
            for (let j = 0; j < i; j++) {
                if (dp[j] && j + nums[j] >= i) {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[n - 1];
    }
    // 시간복잡도 O(N^2)
    // 공간복잡도 O(N)
    function memoFunc(nums: number[]): boolean {
        let memo = new Map<number, boolean>();

        function dfs(start: number): boolean {
            if (start === nums.length - 1) return true;
            if (memo.has(start)) return memo.get(start)!;
            for (let i = 1; i <= nums[start]; i++) {
                if (dfs(start + i)) {
                    memo.set(start, true);
                    return true;
                }
            }

            memo.set(start, false);
            return false;
        }

        return dfs(0);
    }

    // 시간복잡도 O(N)
    // 공간복잡도 O(1)
    function greedyFunc(nums: number[]): boolean {
        let reach = 0;
        for (let i = 0; i < nums.length; i++) {
            if (i <= reach) {
                reach = Math.max(reach, i + nums[i]);
            }
        }

        return nums.length - 1 <= reach;
    }
}
