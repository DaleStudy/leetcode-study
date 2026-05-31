class Solution {
    public int maxProduct(int[] nums) {
        int n = nums.length;
        int[] dpMax = new int[n];
        int[] dpMin = new int[n];

        dpMax[0] = nums[0];
        dpMin[0] = nums[0];
        for (int i = 1; i < n; i++){
            dpMax[i] = Math.max(Math.max(dpMax[i-1]*nums[i], nums[i]), dpMin[i-1]*nums[i]);
            dpMin[i] = Math.min(Math.min(dpMin[i-1]*nums[i], nums[i]), dpMax[i-1]*nums[i]);
        }
        return findMax(dpMax);
    }

    public int findMax(int[] dp) {
        int answer = dp[0];
        for (int i = 0; i < dp.length; i++) {
            answer = Math.max(dp[i], answer);
        }
        return answer;
    }
}

