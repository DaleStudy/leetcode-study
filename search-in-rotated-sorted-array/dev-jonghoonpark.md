- 문제: https://leetcode.com/problems/search-in-rotated-sorted-array/
- time complexity : O(log n)
- space complexity : O(1)
- 블로그 주소 : https://algorithm.jonghoonpark.com/2024/06/03/leetcode-33

```java
public int search(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    while(left <= right) {
        int mid = left + (right - left) / 2;

        if (nums[mid] == target) {
            return mid;
        }

        if(nums[mid] < nums[right]) {
            if (target < nums[mid] || target > nums[right]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        } else {
            if (target < nums[left] || target > nums[mid]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }

    return -1;
}
```
