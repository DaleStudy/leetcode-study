import java.util.*;

/**
 * Finds the length of the longest consecutive elements sequence in an unsorted array.
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
