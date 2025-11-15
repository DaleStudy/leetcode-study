import java.util.HashSet;
import java.util.Set;

class Solution {
    // Problem: 
    // * nums is unsorted
    // * return: length of longest consecutive elements sequence
    // * req: O(N) time
    // Solution:
    // * Time Complexity: O(N)
    // * Space Complexity: O(N)
    public int longestConsecutive(int[] nums) {
        // Time Complexity: O(N)
        // Space Complexity: O(N)
        Set<Integer> uniq = new HashSet<>();
        for(int num : nums) {
            uniq.add(num);
        }

        // Time Complexity: O(N)
        // * nested loop but is O(N) due to skipping non-root element
        int maxLen = 0;
        for(int num : uniq) {
            // skip if num isn't the root(aka first number in the sequence)
            if(uniq.contains(num - 1)) continue;

            // count till end of consecutive sequence
            int len = 1;
            for(int i = 1; uniq.contains(num + i); i++) {
                len++;
            }

            maxLen = Math.max(maxLen, len);
        }

        return maxLen;
    }
}
