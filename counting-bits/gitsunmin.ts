/**
 * https://leetcode.com/problems/counting-bits/
 * time complexity : O(n)
 * space complexity : O(n)
 */
function countBits(n: number): number[] {
    const arr = new Array(n + 1).fill(0);
    for (let i = 1; i <= n; i++) arr[i] = arr[i >> 1] + (i & 1);
    return arr;
}
