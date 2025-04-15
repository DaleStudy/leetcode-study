/**
 * [Problem]: [70] Climbing Stairs
 * (https://leetcode.com/problems/climbing-stairs/description/)
 */

function climbStairs(n: number): number {
    // 시간복잡도 O(n)
    // 공간복잡도 O(n)
    function dpFunc(n: number): number {
        if (n <= 0) return 0;

        let dpArr: number[] = new Array(n);
        dpArr[0] = 1;
        dpArr[1] = 2;

        for (let i = 2; i < n; i++) {
            dpArr[i] = dpArr[i - 1] + dpArr[i - 2];
        }

        return dpArr[n - 1];
    }

    // 시간복잡도 O(n)
    // 공간복잡도 O(1)
    function dpOptimizedFunc(n: number): number {
        if (n <= 0) return 0;
        if (n === 1) return 1;
        if (n === 2) return 2;

        let prev1 = 1;
        let prev2 = 2;

        for (let i = 3; i < n + 1; i++) {
            let currentValue = prev1 + prev2;

            prev1 = prev2;
            prev2 = currentValue;
        }

        return prev2;
    }

    return dpOptimizedFunc(n);
}
