/**
 * 시간 복잡도: O(n)
 *  - 공차가 1인 등차수열, 등차수열의 합 공식 활용하여 기대 값을 계산 -> O(1)
 *  - 주어진 배열을 순회하면서 각 원소의 합을 계산 -> O(n)
 *  - 기대 값에서 실제 각 원소의 합을 빼면 정답 -> O(1)
 *
 * 공간 복잡도: O(1)
 *
 */
class Solution {
    public int missingNumber(int[] nums) {
        int len = nums.length;
        int expectedSum = len * (len + 1) / 2;
        int actualSum = 0;

        for (int num: nums) {
            actualSum += num;
        }

        return expectedSum - actualSum;
    }
}
