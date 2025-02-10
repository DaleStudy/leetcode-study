/**

 input : rotated array
 output : index of target else -1

 4 5 6 7 0 1 2
 target = 6
 return 2

 solution1) brute force
 return index after loop
 tc : O(n)
 sc : O(1)

 solution2)
 separte array into 2 parts to make sure each part is sorted.
 find the rotated point, binary search for target
 O(logn) + O(logn)

 tc : O(logn)
 sc : O(1)
 */
class Solution {
  public int search(int[] nums, int target) {
    int l = 0;
    int r = nums.length - 1;
    while(l < r) {
      int mid = (r - l) / 2 +l;
      if(nums[mid] <= nums[r]) {
        r = mid;
      } else {
        l = mid + 1;
      }
    }
    // determine which part
    int start = 0;
    int end = nums.length - 1;
    if(nums[start] <= target && nums[Math.max(0, l-1)] >= target) {
      end = Math.max(0, l - 1);
    } else if (nums[l] <= target && nums[end] >= target){
      start = l;
    }

    while(start <= end) {
      int mid = (end - start) / 2 + start;
      if(nums[mid] == target) {
        return mid;
      } else if (nums[mid] < target) {
        start = mid + 1;
      } else {
        end = mid - 1;
      }
    }
    return -1;
  }
}
