class Solution {
  // 시간 복잡도: O(log N) - Binary search
  // 공간 복잡도: O(1) - Constant extra space
  public int findMin(int[] nums) {
    int low = 0;
    int high = nums.length - 1;

    while (low < high) {
      int mid = low + (high - low) / 2;

      if (nums[mid] < nums[high]) {
        high = mid;
      } else {
        low = mid + 1;
      }
    }

    return nums[low];
  }
}

