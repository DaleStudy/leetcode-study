class Solution {
    public int maxProduct(int[] nums) {
        if (nums.length == 1)
            return nums[0];
        if (nums.length == 2) {
            return Math.max(nums[0], Math.max(nums[0] * nums[1], nums[1]));
        }

        int len = nums.length;
        int[] max = new int[len];
        int[] min = new int[len];
        int overall = 0;

        max[0] = min[0] = overall = nums[0];

        for (int i = 1; i < len; i++) {
            // 후보 3을 준비
            int justNum = nums[i];
            // 계속 더한 값
            int keep = justNum * max[i-1];
            // 이전 최소에 음수 곱해서 리버스
            int reverse = justNum * min[i-1];

            // max와 min 배열을 업데이트
            max[i] = Math.max(justNum, Math.max(keep, reverse));
            min[i] = Math.min(justNum, Math.min(keep, reverse));

            // overall을 업데이트, 누적 비교로 최대 전역 유지
            overall = Math.max(overall, max[i]);
        }
        return overall;
    }
}
