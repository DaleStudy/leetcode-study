/*
Time complexity: O(N)
Space complexity: O(N)
*/
function missingNumber(nums: number[]): number {
    const numSet = new Set<number>(nums)
    let missNum = 0
    for (let i = 0; i <= nums.length; i++) {
        if (!numSet.has(i)) {
            missNum = i
            break
        }
    }
    return missNum
};
