/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    // 1. nums 배열 0일 때와 1일 때
    if (nums.length === 0) return 0;
    if (nums.length === 1) return nums[0];

    // 2. i=1일 때
    nums[1] = Math.max(nums[0], nums[1]);
    
    // 3. i=2일 때부터 for문 순회
    for (let i=2; i<nums.length; i++) {
        nums[i] = Math.max(nums[i-2] + nums[i], nums[i-1])
    }
    return nums[nums.length-1];
};

// 시간복잡도와 공간복잡도
// 시간복잡도: 배열의 길이 n 만큼 for문 순회하므로 -> O(n)
// 공간복잡도: nums 배열 그대로 수정하여 계산 -> O(1)
