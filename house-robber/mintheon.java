class Solution {
  public int rob(int[] nums) {
    int[] sums = new int[nums.length];

    sums[0] = nums[0];

    if (nums.length > 1) {
      sums[1] = nums[1];
    }

    if (nums.length > 2) {
      sums[2] = nums[0] + nums[2];
    }

    if (nums.length > 3) {
      for (int i = 3; i < nums.length; i++) {
        sums[i] = Math.max(nums[i] + sums[i - 2], nums[i] + sums[i - 3]);
      }
    }

    int max = 0;
    for(int sum : sums) {
      max = Math.max(sum, max);
    }

    return max;
  }
}
