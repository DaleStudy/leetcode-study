class Solution {
  // 시간 복잡도: O(log n)
  // 공간 복잡도: O(1);
  public int search(int[] nums, int target) {
    int left = 0;
    int right = nums.length - 1;

    while(left <= right) {
      int mid = (left + right) / 2;

      if(nums[mid] > nums[nums.length - 1]) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }

    int answer = binarySearch(nums, 0, left - 1, target);

    return answer != -1 ? answer : binarySearch(nums, left, nums.length - 1, target);
  }

  private int binarySearch(int[] nums, int leftIndex, int rightIndex, int target) {
    int left = leftIndex;
    int right = rightIndex;

    while(left <= right) {
      int mid = (left + right) / 2;

      if(nums[mid] == target) {
        return mid;
      } else if (nums[mid] < target) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }

    return -1;
  }
}
