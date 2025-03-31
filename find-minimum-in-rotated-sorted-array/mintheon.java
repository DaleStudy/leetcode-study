class Solution {
  // 시간복잡도: O(n)
  // 공간복잡도: O(1)
  public int findMin(int[] nums) {
    for(int i = 1; i < nums.length; i++) {
      if(nums[i - 1] > nums[i]) {
        return nums[i];
      }
    }

    return nums[0];
  }
}
