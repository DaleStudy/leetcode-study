// time: O(N)
// space: O(1)

class Solution {
    public int missingNumber(int[] nums) {
        int maxValue = 0;
        int sum = 0;
        for (int i = 0; i < nums.length; i++){
            if (maxValue < nums[i]) maxValue = nums[i];
            sum += nums[i];
        }
        int n = Math.max(nums.length, maxValue);

        return (int) (n * (n + 1))/2 - sum;
    }
}

