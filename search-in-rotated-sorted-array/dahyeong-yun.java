/**
 * TC : O(log n)
 *   - 이진 탐색을 수행하기 때문에 log n
 * SC : O(1)
 *   - 별도 유의미한 공간 할당이 없음
 */
class Solution {
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = (left + right) / 2; 

            if(nums[mid] == target) {
                return mid;
            }

            if (nums[left] <= nums[mid]) {
                if(nums[left] <= target && target <= nums[mid])
                    right = mid;
                else
                    left = mid + 1;
            } else {
                if (nums[mid] <= target && target <= nums[right])
                    left = mid;
                else
                    right = mid - 1;
            }
        }
        return -1;
    }
}
