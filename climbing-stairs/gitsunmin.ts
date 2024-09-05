/**
 * https://leetcode.com/problems/climbing-stairs
 * time complexity : O(n)
 * space complexity : O(1)
 */

export const upStairs = (n: number): number => {
    let [l, r] = [1, 2];
    for (let i = 3; i <= n; i++) [l, r] = [r, l + r];

    return r;
};

export function climbStairs(n: number): number {
    if (n <= 2) return n;
    return upStairs(n);
};
