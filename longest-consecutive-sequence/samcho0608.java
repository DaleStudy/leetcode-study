import java.util.HashSet;
import java.util.Set;

class Solution {
    // * nums is unsorted
    // * return: length of longest consecutive elements sequence
    // * req: O(N) time
    public int longestConsecutive(int[] nums) {
        Set<Integer> uniq = new HashSet<>();

        // O(N)
        for(int num : nums) {
            uniq.add(num);
        }

        // O(N)
        int maxLen = 0;
        for(int num : uniq) {
            // 기존에 시작된 consecutive sequence가 있으면 스킵
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
