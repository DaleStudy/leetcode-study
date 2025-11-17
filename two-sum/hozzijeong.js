/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for(let i =0; i < nums.length - 1; i++){
        const first = nums[i];
        for(let j = i + 1; j < nums.length; j++){
            const last = nums[j];

            if((first + last) === target) return [i,j]
        }
    }

    return []
};
