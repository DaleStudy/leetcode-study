/**
 * https://leetcode.com/problems/number-of-1-bits/
 * time complexity : O(log n)
 * space complexity : O(log n)
 */
function hammingWeight(n: number): number {
    return n.toString(2).replaceAll('0', '').length
}
