import java.util.Arrays;

class Solution {
    public int longestConsecutive(int[] nums) {
        int curSeq = 1;
        int maxSeq = -987654321;

        if(nums.length == 0) {
            return 0;
        }

        Arrays.sort(nums);

        int cur = nums[0];
        for(int i = 1; i < nums.length; i++) {
            if(cur == nums[i]) {
                continue;
            }

            if(cur < nums[i] && Math.abs(nums[i] - cur) == 1) {
                curSeq++;
                cur = nums[i];
                continue;
            }

            // NOTE: 수열의 조건이 깨졌을 때
            maxSeq = Math.max(maxSeq, curSeq);
            curSeq = 1;
            cur = nums[i];
        }

        return Math.max(maxSeq, curSeq);
    }
}
