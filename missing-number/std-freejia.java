class Solution {
    public int missingNumber(int[] nums) {

        int totalSum = 0;      
        // 0부터 nums.length 까지 전부 합    
        for (int i = 0; i <= nums.length; i++) {
            totalSum += i;
        }
        // 0부터 n까지 전부 합 
        for (int i = 0; i < nums.length; i++) {
            totalSum -= nums[i];
        }
        
        return totalSum;
    }
}
