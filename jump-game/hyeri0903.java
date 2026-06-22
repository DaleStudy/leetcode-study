class Solution {
    public boolean canJump(int[] nums) {
        /**
        1.문제: last index 에 도달 가능하면 true, 아니면 false return
        2.constraints
        - first index 에서 시작
        - nums.length min = 1, max = 10000
        - value min = 0, max = 100000
        3.solution
        - brute force: 0 index 부터 1, 2, 3번째 등등 시도, time: O(n^2)
        - 가장 먼 index 을 업데이트하면서 체크 : time O(n)
         */
         int n = nums.length;
        int farthest = 0;

        for(int i = 0; i < n; i++) {
            //현재까지 도달 가능한지 체크
            if(i > farthest) {
                return false;
            }
            //도달가능한 가장 먼 인덱스 update
            farthest = Math.max(farthest, i + nums[i]);
        }
        return true;
    }
}
