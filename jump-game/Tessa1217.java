class Solution {

    // 시간 복잡도: O(N), 공간복잡도: O(1)
    public boolean canJump(int[] nums) {

        int maxJump = 0;
        for (int i = 0; i < nums.length; i++) {
            // 최대 점프수로 현재 인덱스에 도달할 수 없다면
            if (i > maxJump) {
                return false;
            }
            maxJump = Math.max(maxJump, i + nums[i]);
            if (maxJump >= nums.length - 1) {
                return true;
            }
        }

        return true;

    }
}

