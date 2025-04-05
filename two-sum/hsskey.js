/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const map = new Map()

    for(let i = 0; i < nums.length; i++) {
        const needNum = target - nums[i]
        if(map.has(needNum)) {
            return [i, map.get(needNum)]
        }

        map.set(nums[i], i)
    }
};
