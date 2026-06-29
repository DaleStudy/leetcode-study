class Solution {
    public int[] twoSum(int[] nums, int target) {
        int length = nums.length;

        for (int first = 0; first < length - 1; first++) {
            for (int second = first + 1; second < length; second++) {
                int sum = nums[first] + nums[second];

                if (sum == target) {
                    return new int[]{first, second};
                }
            }
        }

        return new int[0];
    }
}
