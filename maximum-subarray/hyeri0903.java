class Solution {
    public int maxSubArray(int[] nums) {
        /**
        1. 문제: 가장 큰  합을 가지는 subarray 의 sum 을 반환
        2. 조건: 원소값은 음수 ~ 양수, 배열 최대 길이 = 10^5, 최소 길이 = 1
        - time complexity: O(N)
        - space complexity: O(1)
         */

         if (nums.length == 1) {
            return nums[0];
         }
        
        int maxSum = nums[0];   //전체 최대
        int curSum = nums[0];   //현재 합
 
        for(int i = 1; i<nums.length; i++) {
            curSum = Math.max(nums[i], curSum + nums[i]);
            maxSum = Math.max(maxSum, curSum);
        }
        return maxSum;
    }
}
