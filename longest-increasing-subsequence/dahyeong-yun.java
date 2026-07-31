/**
  * TC : O(n^2)
  *   - 숫자 배열의 길이가 n 일 때 바깥 쪽 루프의 인덱스가 하나씩 증가함에 따라 때 안쪽 루프는 각각 1번, 2번, n-1번 까지 순회함
  *   - 따라서 총 반복 횟수는 1 + 2 + ... + n-1
  *   - 등차급수 합계 공식에 따라 n(n-1) / 2 만큼 반복하므로 시간복잡도는 최고 차항만 고려하여 n^2
  * SC : O(n)
  *   - 숫자 배열 길이 n 만큼의 추가 배열을 공간을 생성하므로 O(n)
  */
class Solution {
    public int lengthOfLIS(int[] nums) {
        int len = nums.length; 
        int[] dp = new int[len]; // 최대 길이는 input 의 길이 만큼임
        Arrays.fill(dp, 1); // 모든 길이는 최소 1

        for(int i=1; i<len; i++) {
            for(int j=0; j<i; j++) {
                if(nums[j] < nums[i]) { // 현재보다 작은 수인 경우, 현재 수를 끝에 붙이는 길이 케이스와 기존 최대값 비교
                    dp[i] = Math.max(dp[j] + 1, dp[i]);
                }
            }
        }

        int max = 1;
        for(int i : dp) {
            max = Math.max(i, max);
        }

        return max;
    }
}
