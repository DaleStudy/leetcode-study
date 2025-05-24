import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int characterReplacement(String s, int k) {
        int maxLen = 0;
        int maxCount = 0;
        Map<Character, Integer> counter = new HashMap<>();
        int start = 0;

        for (int end = 0; end < s.length(); end++) {
            char endChar = s.charAt(end);
            counter.put(endChar, counter.getOrDefault(endChar, 0) + 1);
            maxCount = Math.max(maxCount, counter.get(endChar));

            while (end - start + 1 - maxCount > k) {
                char startChar = s.charAt(start);
                counter.put(startChar, counter.get(startChar) - 1);
                start++;
            }

            maxLen = Math.max(maxLen, end - start + 1);
        }

        return maxLen;
    }
}


