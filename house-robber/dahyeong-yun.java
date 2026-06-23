/**
 * [문제 분석 및 풀이]
 * 1. 시간 복잡도
 * - 배열의 원소가 $10^2$개 있으므로 O(N^3)도 가능할 수 있음
 * 2. 제약 사항
 * - 문제의 메인 컨셉인 건너 뛰어서 합산하는 것 외에 딱히 고려할 제약은 없어 보임
 * 3. 풀이 아이디어 : DP
 * - 하루 걸러서 털 수 있으므로, 이전까지의 최대값에 오늘 터는 경우를 더한 것과, 어제까지 털었을 경우 두 가지의 비교로 최대 이익을 구할 수 있다.
 * - 오늘의 max = (오늘 털면 얻는 이득 + 전전날 까지 max, 어제까지 max)
 * - 자연스럽게 동적계획법 형태로 풀이.
 */
class Solution {
    public int rob(int[] nums) {
        int len = nums.length;

        // 3일 이하 예외 처리
        if(len == 1) return nums[0];
        if(len == 2) return Math.max(nums[0], nums[1]);

        int[] dp = new int[len];
        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);

        // 메모제이션
        for(int i = 2; i < len; i++) {
            dp[i] = Math.max(dp[i-1], dp[i-2] + nums[i]);
        }
        return dp[len - 1];
    }
}
