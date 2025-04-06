import java.util.Arrays;

class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        Arrays.sort(nums);

        int answer = 1;
        int current = 1;
        for (int i=1; i<nums.length; i++) {
            // 이전 숫자와 같다면 스킵
            if (nums[i-1] == nums[i]) {
                continue;
            }

            // 연속된 숫자라면 증가, 아니라면 초기화
            if (nums[i-1] + 1 == nums[i]) {
                current++;
                answer = Math.max(answer, current);

            } else {
                current = 1;
            }
        }

        return answer;
    }
}
