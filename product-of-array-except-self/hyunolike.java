class Solution {
    public int[] productExceptSelf(int[] nums) {

        int n = nums.length;
        int[] ans = new int[n];

        // 1. 왼족 곱
        int left = 1;
        for(int i = 0; i < n; i++) {
            ans[i] = left;
            left *= nums[i];
        }

        // 2. 오른쪽 곱
        int right = 1;
        for(int i = n-1; i >=0; i--){
            ans[i] *= right;
            right *= nums[i];
        }

        return ans;
    }
}
