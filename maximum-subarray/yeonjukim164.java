class Solution {
    public int maxSubArray(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }

        int currentSum = nums[0];
        int maxSum = nums[0];

        for (int i = 1; i < nums.length; i++) {
            // 현재까지의 연속 합을 이어갈지, 새로 시작할지 결정
            currentSum = Math.max(nums[i], currentSum + nums[i]);

            // 전역 최대값 업데이트
            maxSum = Math.max(maxSum, currentSum);
        }

        return maxSum;
    }
}
