class Solution {
    // 최소값은 음수가 곱해질 때 최대값이 될 수 있기 때문에 최소, 최대를 각각 dp[]로 관리해야 한다.
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
            /**
             * 현재 인덱스값 (justNum)
             * 이전 인덱스 최소값 x 현재 인덱스 값 (reverse)
             * 이전 인덱스 최대값 x 현재 인덱스 값 (keep)
             */
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
