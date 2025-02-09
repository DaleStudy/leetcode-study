// 시간 복잡도: DP -> O(N)
// 공간 복잡도: nums 배열 크기 - O(N)

class Solution {
    public int maxSubArray(int[] nums) {
        int currentSum = nums[0];
        int maxSum = currentSum;
        for (int i = 1; i < nums.length; ++i) {
            currentSum = Math.max(currentSum + nums[i], nums[i]);
            maxSum = Math.max(maxSum, currentSum);
        }

        return maxSum;
    }
}
