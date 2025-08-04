// [참고]
// 카데인 알고리즘: 이전요소의 부분합을 알면 현재요소의 최대값을 알 수 있다.
// 양수만이라면 단순히 dp로 dp[nums.length-1] 값이나 total이라는 계산값을 리턴하겠지만,
// 음수가 포함되었으므로 bestSum과 currentSum을 별개의 변수로 처리한다.
// currentSum은 최대 sum을 구해야 하므로 음수값일때 강제로 0으로 업데이트 후 계산을 실행한다.
// https://velog.io/@wind1992/Leetcode-53.-Maximum-Subarray
//
// [풀이방식]
// 1. 카데인 알고리즘 2. DP
// [성능]
// dp 배열보다 변수를 사용하는 것이 공간 복잡도를 줄일 수 있다. 또한 for문 1개로 해결 가능하다.
class Solution {
    public int maxSubArray(int[] nums) {
        int bestSum = nums[0];
        int currentSum = 0;

        for (int n : nums) {
            if (currentSum < 0) { // 1. 업데이트
                currentSum = 0;
            }

            // 2. 계산
            currentSum += n;
            bestSum = Math.max(currentSum, bestSum);
        }
        return bestSum;
    }

    public int maxSubArrayDp(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];

        dp[0] = nums[0];
        int maxSum = dp[0];

        for (int i = 1; i < n; i++) {
            dp[i] = Math.max(nums[i], dp[i - 1] + nums[i]);
            maxSum = Math.max(maxSum, dp[i]);
        }

        return maxSum;
    }
}
