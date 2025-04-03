/**
 * 주어진 배열에서 인접하지 않은 숫자들의 최대 합을 반환하는 함수
 * @param {number[]} nums
 * @return {number}
 */
const rob = function(nums) {
    const dp = [];

    nums.forEach((num, idx) => {
        dp[idx] = Math.max((dp[idx - 2] || 0) + num, dp[idx - 1] || 0);
    });

    return dp[dp.length - 1];
};

// 시간복잡도: O(n);
// 공간복잡도: O(n);
