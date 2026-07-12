/**
 * [풀이 개요]
 * - 시간복잡도 : O(n)
 * - 공간복잡도 : O(1)
 */
class Solution {
    /**
     * [문제 풀이 아이디어]
     * - 연속된 부분 배열 합의 최대를 구하는 문제. 즉, 카데인 알고리즘을 떠올릴 수 있음
     * - 수 배열을 한번 순회 하므로 시간복잡도는 O(n)
     * - 별도 공간 할당이 없으므로 공간복잡도는 O(1)
     */
    public int maxSubArray(int[] nums) {
        int max = nums[0];
        int current = nums[0];

        int len = nums.length;
        for(int i=1; i<len; i++) {
            current = Math.max(nums[i], current + nums[i]);
            max = Math.max(current, max);
        }

        return max;
    }
}
