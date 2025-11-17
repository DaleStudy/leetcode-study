/**
 * Runtime: 0ms
 * Time Complexity: O(n)
 *
 * Memory: 42.72MB
 * Space Complexity: O(1)
 *
 * Approach: 두 가지 변수만 사용한 DP 접근법
 * - withoutPrevHouse: 이전 집을 털지 않았을 때의 최대 금액
 * - withPrevHouse: 이전 집까지 고려한 최대 금액
 * - 각 집에서 "털거나 안 털거나" 두 가지 선택지 중 최대값 선택
 * 1) 현재 집을 안 털면: 이전 집까지의 최대값 유지
 * 2) 현재 집을 털면: 전전 집까지의 최대값 + 현재 집 금액
 */
class Solution {
    public int rob(int[] nums) {
        int withoutPrevHouse = 0;
        int withPrevHouse = 0;

        for (int money: nums) {
            int maxMoney = Math.max(withPrevHouse, withoutPrevHouse+money);
            withoutPrevHouse = withPrevHouse;
            withPrevHouse = maxMoney;
        }

        return withPrevHouse;
    }
}
