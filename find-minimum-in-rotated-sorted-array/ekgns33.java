/**
 input : array of integers
 output : minimum element's value

 3 4 5 1 2
 draw graph

 5
 4
 3
 2
 1
 l    r
 l    r
 l            r
 --------------
 5
 4
 3
 2
 1
 mid  right
 --------------
 left < right ->> sorted.
 left < mid ->>  don't have to search range [left, mid]
 mid > right ->> rotation point is between [mid, right];

 solution 1) brute force
 read the array

 tc : O(n)
 sc : O(1);

 solution 2) binary search
 do binary search, move pointers with descripted conditions
 after binary search loop ends, the left pointer is the minimum element

 tc : O(logn)
 sc : O(1)
 */

class Solution {
  public int findMin(int[] nums) {
    int l = 0;
    int r = nums.length - 1;
    while(l < r) {
      int mid = (r - l) / 2 + l;
      if(nums[mid] < nums[r]) {
        r = mid;
      } else {
        l = mid + 1;
      }
    }
    return nums[l];
  }
}
