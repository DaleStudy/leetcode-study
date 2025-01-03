/**
 * 시간 복잡도: 최대 nums의 길이만큼 순회하므로, O(n)
 * 공간 복잡도: map은 최대 nums의 길이 - 1 만큼의 공간을 차지하므로, O(n)
 */
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const map = new Map();
    
    for(let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if(map.has(complement)) {
            return [i, map.get(complement)]
        }
        map.set(nums[i], i);
    }
};
