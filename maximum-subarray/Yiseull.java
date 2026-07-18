class Solution {
    public int maxSubArray(int[] nums) {
        int answer = -10001, tmp = 0;

        for (int i = 0; i < nums.length; i++) {
            tmp += nums[i];
            answer = Math.max(answer, tmp);
            tmp = Math.max(tmp, 0);
        }

        return answer;
    }
}
