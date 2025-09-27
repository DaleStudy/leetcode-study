class Solution {
  bool canJump(List<int> nums) {
    for (int i = 0, j = 0; j < nums.length - 1; i++) {
        if (j < i) {
            return false;
        }
        j = max(i + nums[i], j);
    }
    return true;
  }
}
