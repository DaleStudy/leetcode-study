// 시간복잡도: O(n)
// 공간복잡도: O(1)

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    let fast = 0;

    for (let i = 0; i < nums.length; i++) {
        if (i > 0 && i > fast) return false

        fast = Math.max(fast, i + nums[i])

        if (fast >= nums.length -1) return true
    }

    return false
};
