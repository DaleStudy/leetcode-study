/**
 * 정수 배열 nums가 주어질 때 가장 길게 증가하는 부분 수열의 길이를 찾으세요. (LIS)
 */
class Solution {

    // 시간복잡도: O(n^2)
    public int lengthOfLIS(int[] nums) {

        int[] dp = new int[nums.length];
        int n = nums.length;
        int max = 0;

        // 원소의 위치에서 가질 수 있는 LIS의 값 계산
        for (int i = 0; i < n; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            max = Math.max(dp[i], max);
        }

        return max;
    }
}

