class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        int[] sum = new int[n];

        int minValue = 0;
        int answer = nums[0];

        for (int i = 0; i < n; i++){
            if (i == 0) sum[i] = nums[i];
            else sum[i] = sum[i-1] + nums[i];
        }

        for (int i = 0 ; i < n; i++){
            answer = Math.max(answer, sum[i] - minValue);
            if (minValue > sum[i]){
                minValue = sum[i];
            }
        }
        return answer;

    }
}


