class Solution {
  /**
   시간복잡도: O(n)
   공간복잡도: O(1)
   */
  public int missingNumber(int[] nums) {
    int n = nums.length;
    int expectedSum = n * (n + 1) / 2;

    int arraySum = 0;
    for(int i = 0; i < nums.length; i++) {
      arraySum += nums[i];
    }

    return expectedSum - arraySum;
  }
}
