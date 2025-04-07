/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const map = new Map()

    for(let i = 0; i < nums.length; i++) {
        if(map.has(nums[i])) {
            const prevVal = map.get(nums[i])
            map.set(nums[i], prevVal + 1)
        } else {
            map.set(nums[i], 1)
        }
    }

    const result = [...map.entries()].sort((a, b) => b[1] - a[1]).slice(0, k).map((item) => {
        return item[0]
    })
    return result
};
