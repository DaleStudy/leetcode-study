class Solution {
    // TC : O(n)
    // SC : O(1)
    public int maxSubArray(int[] nums) {
        int max = nums[0];
        int sum = 0;

        for (int i = 0; i < nums.length; i++) {
            // 부분합보다 현재 숫자가 더 크면 갱신한다.
            // 현재 숫자 단독이 더 큰 경우 이전 합이 의미가 없기 때문에 그리디하게 처리 가능
            sum = Math.max(nums[i], nums[i] + sum);
            max = Math.max(sum, max);
        }

        return max;
    }
}
