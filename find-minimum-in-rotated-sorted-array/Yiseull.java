class Solution {
    public int findMin(int[] nums) {
        return binarySearch(nums);
    }

    // 공간복잡도: O(1), 시간복잡도: O(logn)
    private int binarySearch(int[] nums) {
        int left = 0, right = nums.length - 1;
        int answer = 5000;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (nums[right] <= nums[left] && nums[left] <= nums[mid]) {
                answer = Math.min(answer, nums[mid]);
                left = mid + 1;
            }
            else {
                answer = Math.min(answer, nums[mid]);
                right = mid - 1;
            }
        }

        return answer;
    }
}
