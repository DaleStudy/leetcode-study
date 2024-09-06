// 시간 복잡도 O(n log n)
// 공간 복잡도 O(n)

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    if (nums.length === 0) return []

    let maxSequenceLength = -Infinity


    const setNums = [...new Set(nums)].toSorted((a,b) => a - b)

    let count = 0;
    for (let i = 0 ; i < setNums.length; i++) {
        if (setNums[i]+1 === setNums[i+1]) {
            count += 1
        } else {
            count += 1
            maxSequenceLength = Math.max(maxSequenceLength, count)
            count = 0;
        }
    }

    return maxSequenceLength
};


console.log(longestConsecutive([100,4,200,1,3,2]))
console.log(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
