/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function (nums) {
    const dp = new Array(nums.length).fill(false);

    dp[0] = true;

    for (let i = 0; i < nums.length; i++) {
        if (!dp[i]) {
            continue;
        }

        for (let j = 1; j < nums[i] + 1; j++) {
            if (i + j >= nums.length) {
                break;
            }

            dp[i + j] = true;
        }
    }

    return dp[dp.length - 1];
};

// 시간복잡도 O(n2) -> nums의 길이대로 순회하면서 1부터 nums[j]의 값까지 순회하는 2중 루프를 돌기 때문
// 공간복잡도 0(n) -> nums의 길이에 따라 dp 배열의 길이가 결정되므로
