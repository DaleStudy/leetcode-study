/*
time complexity : O(n^2)
space complexity : O(1)
*/
function threeSum(nums: number[]): number[][] {
    const result: number[][] = []
    const sortedNums = nums.sort((a, b) => a - b)

    for(let i = 0; i < sortedNums.length - 2; i++) {
        if (i > 0 && sortedNums[i] === sortedNums[i - 1]) continue
        let low = i + 1
        let high = sortedNums.length - 1
        while (low < high) {
            const threeSum = sortedNums[i] + sortedNums[low] + sortedNums[high]
            if (threeSum < 0) {
                low += 1
            } else if (threeSum > 0) {
                high -= 1
            } else {
                result.push([sortedNums[i], sortedNums[low], sortedNums[high]])
                while (low < high && sortedNums[low] === sortedNums[low + 1]) low++
                while (low < high && sortedNums[high] === sortedNums[high - 1]) high--

                low += 1
                high -= 1
            }
        }
    }
    return result
};