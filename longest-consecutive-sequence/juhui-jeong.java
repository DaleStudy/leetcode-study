class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums == null || nums.length == 0) return 0;
        Arrays.sort(nums);

        int maxLen = 1;
        int curLen = 1;

        for(int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i-1]) {
                // 중복 건너뛰기
                continue;
            }

            if (nums[i] == nums[i-1] +1) {
                curLen++;
            } else {
                maxLen = Math.max(maxLen, curLen);
                curLen = 1;
            }
        }

        return Math.max(maxLen, curLen);
    }
}
