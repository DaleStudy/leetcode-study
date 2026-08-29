import java.util.*;

// TC: O(n log n)
// SC: O(n)
class Solution {
    public int lengthOfLIS(int[] nums) {

        // tails[k] = 길이 k+1인 증가 부분수열의 최소 끝값 → 오름차순이라 이진 탐색 가능
        // 예) [1,3,5,2] → tails=[1,2,5]. 배열 자체는 부분수열이 아니고 길이 3이 정답
        int[] tails = new int[nums.length];
        int size = 0;

        for (int num : nums) {
            int idx = Arrays.binarySearch(tails, 0, size, num);
            int pos = idx >= 0 ? idx : -idx - 1;

            tails[pos] = num;
            size = Math.max(size, pos + 1);
        }

        return size;
    }
}

// 첫 번째 풀이 — O(n^2) DP (TC: O(n^2), SC: O(n))
// dp[i] = nums[i]에서 끝나는 증가 부분수열의 최대 길이
//
// public int lengthOfLIS(int[] nums) {
//     int n = nums.length;
//     int[] dp = new int[n];
//     int answer = 0;
//
//     for (int i = 0; i < n; i++) {
//         int prevLongest = 0;
//         for (int j = 0; j < i; j++) {
//             if (nums[j] < nums[i]) {
//                 prevLongest = Math.max(prevLongest, dp[j]);
//             }
//         }
//         dp[i] = prevLongest + 1;
//         answer = Math.max(answer, dp[i]);
//     }
//
//     return answer;
// }
