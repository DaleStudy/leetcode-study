import java.util.*;

class Solution {
    // TC: O(n)
    // SC: O(n)
    public int longestConsecutive(int[] nums) {
        // 연속적인 수의 개수를 구한다.
        Arrays.sort(nums);
        int maxCount = 0;
        int cur = 1;
        for ( int i = 1 ; i < nums.length; i ++){
            if (nums[i] == nums[i - 1]) {
                continue;                       // 중복 건너뛰기
            } else if (nums[i - 1] + 1 == nums[i]) {
                cur += 1;
            } else {
                cur = 1;
            }
            maxCount = Math.max(maxCount, cur); // 매 스텝마다 갱신
        }
        return maxCount;
    }
}
