/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    if(nums.length === 1) {
        return nums[0]
    }

    if(nums[0] < nums[nums.length -1]) {
        return nums[0]
    }

    let left = 0
    let right = nums.length - 1

    while(left < right) {
        const mid = Math.floor((left + right) / 2)

        if(nums[mid] > nums[right]) {
            left = mid + 1
        } else {
            right = mid
        }
    }
    return nums[left]
};
