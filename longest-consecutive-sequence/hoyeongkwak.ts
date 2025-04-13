/*
시간복잡도 : O(n)
공간복잡도 : O(n)
*/
function longestConsecutive(nums: number[]): number {
    const numSet = new Set<number>()
    let maxLen = 0
    nums.forEach((num) => {
        numSet.add(num)
    })

    for (const num of numSet) {
        if (!numSet.has(num - 1)) {
            let continueCnt = 1
            let current = num
            
            while (numSet.has(current + 1)) {
                current++
                continueCnt++
            }
            maxLen = Math.max(continueCnt, maxLen)
        }
    }
    return maxLen
};