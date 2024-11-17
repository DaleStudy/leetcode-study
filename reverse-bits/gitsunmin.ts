/**
 * https://leetcode.com/problems/reverse-bits/
 * time complexity : O(1)
 * space complexity : O(1)
 */

function reverseBits(n: number): number {
    let result = 0;
    for (let i = 0; i < 32; i++) {
        result <<= 1;
        result |= n & 1;
        n >>>= 1;
    }
    return result >>> 0;
};
