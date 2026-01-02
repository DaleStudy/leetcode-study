public class Solution {
    public int maxSubArray(int[] nums) {
        int max = Integer.MIN_VALUE;
        for(int i = 0; i < nums.length; i++) {
            for (int j = i; j < nums.length; j++) {
                int sum = 0;
                for(int k = i; k <= j; k++) {
                    sum+= nums[k];
                }
                max = Math.max(max, sum);
            }
        }
        return max;
    }
}
