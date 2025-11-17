class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        boolean[] dp = new boolean[n+1];

        for(int i=0; i<n; i++) {
            dp[nums[i]]=true;
        }

        for(int i=0; i<=n; i++) {
            if(dp[i]==false) return i;
        }
        return 0;
    }
}

