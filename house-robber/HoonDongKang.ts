/**
 * [Problem]: [198] House Robber
 * (https://leetcode.com/problems/house-robber/description/)
 */
function rob(nums: number[]): number {
    // 시간 복잡도 O(2^n)
    // 공간 복잡도 O(n)
    // 시간 초과
    function recursionFunc(nums: number[]): number {
        function getMax(start: number): number {
            if (nums.length - 1 < start) return 0;
            return Math.max(nums[start] + getMax(start + 2), getMax(start + 1));
        }

        return getMax(0);
    }

    // 메모이제이션
    // 시간복잡도 O(n)
    // 공간복잡도 O(n)
    function memoizationFunc(nums: number[]): number {
        let memoArr = new Array(nums.length).fill(-1);
        function getMax(start: number): number {
            if (nums.length - 1 < start) return 0;
            if (memoArr[start] !== -1) return memoArr[start];

            memoArr[start] = Math.max(nums[start] + getMax(start + 2), getMax(start + 1));

            return memoArr[start];
        }

        return getMax(0);
    }

    // DP
    // 시간복잡도 O(n)
    // 공간복잡도 O(1)
    function dpSolution(nums: number[]): number {
        if (nums.length === 1) return nums[0];

        let prev2 = 0;
        let prev1 = 0;

        for (let num of nums) {
            let current = Math.max(prev1, prev2 + num);
            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }

    return dpSolution(nums);
}
