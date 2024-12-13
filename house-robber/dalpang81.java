//시간복잡도 O(n)
class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }

        int temp2 = nums[0];
        int temp1 = Math.max(nums[0], nums[1]);

        for (int i = 2; i < nums.length; i++) {
            int current = Math.max(temp1, nums[i] + temp2);
            temp2 = temp1;
            temp1 = current;
        }

        return temp1;
    }
}
