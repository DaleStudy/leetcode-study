/**
  배열은 강도가 털 집의 돈을 순서대로 나타냅니다.
 *
 * 인접한 두 집을 동시에 털면 경찰에 알림이 가기 때문에 피해야 합니다.
 *
 * 하루에 훔칠 수 있는 가장 많은 돈을 구하는 문제입니다.
 *
 *
 * 2. naive 알고리즘 도출
 *
 * - 현재 집을 털기 → 바로 이전 집은 못 털었으므로 prev2 + 현재집
 * - 현재 집을 안 털기 → 이전까지의 최댓값 유지 prev1
 */
class sangyyypark {
    public static int rob(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        if (nums.length == 1) {
            return nums[0];
        }


        int prev2 = 0;  // i-2번째 집까지의 최대 금액
        int prev1 = 0;  // i-1번째 집까지의 최대 금액

        for (int num : nums) {
            // 현재 집을 털 경우: prev2 + num
            // 현재 집을 안 털 경우: prev1
            int current = Math.max(prev1, prev2 + num);


            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }
}

