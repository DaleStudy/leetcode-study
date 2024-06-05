- 문제: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
- time complexity : O(log n)
- space complexity : O(1)
- 블로그 주소 : https://algorithm.jonghoonpark.com/2024/06/03/leetcode-153

```java
public int findMin(int[] nums) {
    int left = 0, right = nums.length - 1;
    while(left < right) {
        int mid = left + (right - left) / 2;

        if(nums[mid] < nums[right]) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    return nums[left];
}
```
