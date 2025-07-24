/**
 * solve 1
 *
 * 시간 복잡도: O(n^2)
 * 공간 복잡도: O(1)
 *
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const length = nums.length - 1;

    for (let i = 0; i < length; i++) {
        for(let j = length; j > 0; j--) {
            const sum = nums[i] + nums[j];

            if (i !== j) {
                if (sum === target) {
                    return [i , j];
                }
            }
        }
    }
};


/**
 * solve 2
 *
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(n)
 *
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const map = new Map();

    for (let i = 0; i < nums.length; i++) {
        const temp = target - nums[i];

        if (map.has(temp)) {
            return [map.get(temp), i];
        }

        map.set(nums[i], i);
    }
};
