import java.util.*;

class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> table = new HashSet<>();
        int longest = 0;

        for(int n : nums) {
            table.add(n);
        }

        // O(N)
        for (int num : table) {
            if (!table.contains(num - 1)) {
                int currentNum = num;
                int currentStreak = 1;

                while (table.contains(currentNum + 1)) {
                    currentNum++;
                    currentStreak++;
                }
                longest = Math.max(longest, currentStreak);
            }
        }

        /** TIME OUT 발생!
         *
        for (int n : nums) {
            if (table.contains(n - 1)) continue;
            int len = 1;
            while (table.contains(n + len)){
                len++;
            }
            longest = Math.max(len, longest);
        }
         */

        return longest;
    }
}
