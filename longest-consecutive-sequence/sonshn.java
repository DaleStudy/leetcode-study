import java.util.*;

/**
 * 주어진 배열에서 연속된 정수의 가장 긴 길이를 찾는 문제
 * 
 * 시간 복잡도: O(n log n), 공간 복잡도: O(1)
 */
class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }

        Arrays.sort(nums);

        int longest = 0;
        int length = 1;

        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                continue;
            }

            if (nums[i] + 1 == nums[i + 1]) {
                length++;
            } else {
                longest = Math.max(longest, length);
                length = 1;
            }
        }

        longest = Math.max(longest, length);
        return longest;
    }
}
