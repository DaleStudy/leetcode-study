class Solution {
    public int findMin(int[] nums) {
        return binarySearch(nums, 0, nums.length -1);
    }

    private int binarySearch(int[] nums, int left, int right) {
        // 탐색 범위에 원소가 하나만 남은 경우
        if (left == right) {
            return nums[left];
        }

        // [1] 현재 범위가 이미 오름차순이라면 첫 번째 값이 최솟값!
        if (nums[left] < nums[right]) {
            return nums[left];
        }

        int mid = left + (right - left) / 2;
        // [2-1] 왼쪽 구간이 정렬되어 있다면 최솟값은 오른쪽 구간에 있다
        if (nums[left] <= nums[mid]) {
            return binarySearch(nums, mid + 1, right);
        }
        // [2-2] 회전 지점이 왼쪽 구간에 있다.
        return binarySearch(nums, left, mid);
    }
}
