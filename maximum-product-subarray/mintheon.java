class Solution {
  //시간복잡도: O(n)
  //공간복잡도: O(n)
  public int maxProduct(int[] nums) {
    int[] maxValue = new int[nums.length];
    int[] minValue = new int[nums.length];

    maxValue[0] = nums[0];
    minValue[0] = nums[0];

    for(int i = 1; i < nums.length; i++) {
      int value1 = maxValue[i - 1] * nums[i];
      int value2 = minValue[i - 1] * nums[i];

      maxValue[i] = Math.max(Math.max(value1, value2), nums[i]);
      minValue[i] = Math.min(Math.min(value1, value2), nums[i]);
    }

    int result = Integer.MIN_VALUE;
    for(int i = 0; i < nums.length; i++) {
      result = Math.max(result, maxValue[i]);
    }

    return result;
  }
}
