/**
 * 주어진 배열에서 가장 긴 증가하는 수열의 길이를 반환하는 함수
 * @param {number[]} nums
 * @return {number}
 */
const lengthOfLIS = function (nums) {
    const dp = Array(nums.length).fill(1);

    for (let i = 0; i < nums.length; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[j] < nums[i])
                dp[i] = Math.max(dp[j] + 1, dp[i]);
        }
    }

    return Math.max(...dp);
};

// 시간복잡도: O(n^2)
// 공간복잡도: O(n)
