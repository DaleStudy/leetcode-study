/**
 * Runtime: 3ms
 * Time Complexity: O(n log n)
 * - 각 요소마다 이분 탐색
 *
 * Memory: 45.99MB
 * Space Complexity: O(n)
 *
 * Approach: Patience Sorting, 각 원소를 순서대로 확인하며 현재까지 만든 가장 유리한 수열 계산
 * - result의 모든 원소보다 크면 맨 뒤에 추가
 * - 그렇지 않으면, 이분 탐색으로 나온 위치에 값을 대체
 */
class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] result = new int[nums.length];
        int resultSize = 0;

        for (int num : nums) {
            int left = 0;
            int right = resultSize;

            while (left < right) {
                int mid = left + (right-left) / 2;
                if (result[mid] < num) {
                    left = mid+1;
                } else {
                    right = mid;
                }
            }

            result[left] = num;

            if (left == resultSize) {
                resultSize++;
            }
        }

        return resultSize;
    }
}
