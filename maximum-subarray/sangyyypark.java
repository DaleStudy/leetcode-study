class sangyyypark {
    public int maxSubArray(int[] nums) {
        int sum = nums[0];
        int max = sum;
        for(int i = 1; i < nums.length; i++) {
            if(sum + nums[i] < nums[i]) {
                sum = nums[i];
            }
            else {
                sum+=nums[i];
            }
            max = Math.max(sum,max);
        }

        return max;
    }
}

