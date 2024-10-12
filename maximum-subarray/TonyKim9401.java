// TC: O(n)
// visit all elements once for each
// SC: O(1)
// constant space occupation
class Solution {
    public int maxSubArray(int[] nums) {
        int total = 0;
        int output = nums[0];

        for (int num : nums) {
            if (total < 0) total = 0;
            total += num;
            output = total > output ? total : output;
        }
        return output;
    }
}
