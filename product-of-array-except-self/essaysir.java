class Solution {
    public int[] productExceptSelf(int[] nums) {
        // 시간 복잡도가 O(N) 이어야 함.
        // 배열에서 나 자신을 빼고서 모두를 곱하라
        // 어떻게 해야 시간 복잡도가 O(N) 이지 ?
        int n = nums.length;
        int zeroCount = 0;
        int maxTotal = 1; // 0이 아닌 값들의 곱
        for (int x : nums) {
            if (x == 0) zeroCount++;
            else maxTotal *= x;
        }

        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            if (zeroCount >= 2) {
                result[i] = 0;                          // 0이 2개 이상 → 무조건 0
            } else if (zeroCount == 1) {
                result[i] = (nums[i] == 0) ? maxTotal : 0; // 0 위치만 살아남음
            } else {
                result[i] = maxTotal / nums[i];          // 0 없음 → 그냥 나눔
            }
        }
        return result;
    }
}
