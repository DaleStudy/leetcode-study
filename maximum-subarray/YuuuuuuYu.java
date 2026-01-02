/**
 * Runtime: 1ms
 * Time Complexity: O(n)
 *
 * Memory: 76.88MB
 * Space Complexity: O(1)
 *
 * Approach: 카데인 알고리즘
 * - 부분 배열의 합이 최대가 되는 값을 찾는 알고리즘
 * 1) 이전 합보다 현재 숫자가 더 크면 현재 숫자로 sum을 초기화
 */
class Solution {
    public int maxSubArray(int[] nums) {
        int sum = nums[0];
        int max = nums[0];

        for (int i=1; i<nums.length; i++) {
            sum = Math.max(nums[i], sum+nums[i]);
            max = Math.max(max, sum);
        }

        return max;
    }
}
