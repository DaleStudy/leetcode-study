/*
https://leetcode.com/problems/house-robber/
 */
class Solution{
    public int rob(int[] nums){
        if(nums.length == 0 || nums == null) return 0;
        if(nums.length == 1) return 0;

        int prev1 = 0;
        int prev2 = 0;
        for(int num: nums){
            int temp = Math.max(prev1, prev2+num);
            prev2 = prev1;
            prev1 = temp;
        }

        return prev1;
    }
}


