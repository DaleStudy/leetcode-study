/*
Time Complexity: O(n)
Space Complexity: O(n)
*/
function countBits(n: number): number[] {
    const result: number[] = new Array(n + 1).fill(0)
    for(let i = 1; i <= n; i++) {
        result[i] = result[i >> 1] + (i & 1)
    }
    return result
};
