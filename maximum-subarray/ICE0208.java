class Solution {
    /**
     * 배열을 절반으로 나누고 최대 부분 배열이
     * 왼쪽, 오른쪽, 가운데를 걸치는 경우를 각각 구한다.
     *
     * 시간 복잡도: O(n log n)
     * 공간 복잡도: O(log n)
     */
    public int maxSubArray(int[] nums) {
        return findMaxSum(nums, 0, nums.length - 1);
    }

    private int findMaxSum(int[] nums, int left, int right) {
        if (left == right) {
            return nums[left];
        }

        int mid = left + (right - left) / 2;

        int leftMaxSum = findMaxSum(nums, left, mid);
        int rightMaxSum = findMaxSum(nums, mid + 1, right);
        int crossingMaxSum = findCrossingMaxSum(nums, left, mid, right);

        return Math.max(
            Math.max(leftMaxSum, rightMaxSum),
            crossingMaxSum
        );
    }

    private int findCrossingMaxSum(
        int[] nums,
        int left,
        int mid,
        int right
    ) {
        int sum = 0;
        int leftMaxSum = Integer.MIN_VALUE;

        for (int i = mid; i >= left; i--) {
            sum += nums[i];
            leftMaxSum = Math.max(leftMaxSum, sum);
        }

        sum = 0;
        int rightMaxSum = Integer.MIN_VALUE;

        for (int i = mid + 1; i <= right; i++) {
            sum += nums[i];
            rightMaxSum = Math.max(rightMaxSum, sum);
        }

        return leftMaxSum + rightMaxSum;
    }
}
