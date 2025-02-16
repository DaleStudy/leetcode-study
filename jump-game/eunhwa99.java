class Solution {

  public boolean canJump(int[] nums) {
    int furthestIndex = 0;
    for (int i = 0; i < nums.length; i++) {
      if (furthestIndex < i) {
        return false;
      }

      furthestIndex = Math.max(furthestIndex, i + nums[i]);
    }
    return true;
  }
}
