class Solution {
    public int rob(int[] nums) {
        int[] sum = new int[nums.length+1];
        sum[0] = nums[0];
        if(nums.length>1) sum[1] = Math.max(nums[0], nums[1]);
        for(int i=2; i<nums.length; i++){
            sum[i]=Math.max(nums[i]+sum[i-2],sum[i-1]);
        }
        return sum[nums.length-1];
    }
}
