class Solution {
    public int longestConsecutive(int[] nums) {
        // 연속된 숫자 길이 파악
        // 연속된 거 어떻게?
        if(nums.length == 0 || nums == null) return 0;

        int result = 0;

        Arrays.sort(nums);

        int maxLen = 1;
        int len = 1;

        for(int i = 1; i < nums.length; i++) {
            // 중복 체크
            if(nums[i] == nums[i-1]) {
                continue;
            }else if(nums[i] == nums[i-1] + 1) {
                len++;
                maxLen = Math.max(maxLen, len);
            }else{
                len = 1;
            }
        }

        return maxLen;
    }
}
