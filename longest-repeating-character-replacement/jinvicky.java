import java.util.HashMap;
import java.util.Map;

class Solution {
    public int characterReplacement(String s, int k) {
        Map<Character, Integer> charCount = new HashMap<>();

        int left = 0;
        int maxFrequency = 0;
        int maxLength = 0;

        for(int right = 0; right < s.length(); right++) {
            char rightChar = s.charAt(right);

            charCount.put(rightChar, charCount.getOrDefault(rightChar, 0) + 1);

            maxFrequency = Math.max(maxFrequency, charCount.get(rightChar));

            if((right - left + 1) - maxFrequency > k) {
                char leftChar = s.charAt(left);

                charCount.put(leftChar, charCount.get(leftChar) - 1);
                left++;
            }

            maxLength = Math.max(maxLength, right - left + 1);
        }
        return maxLength;
    }

    // while문과 배열로 성능이 개선된 풀이
    public int characterReplacement2(String s, int k) {
        int left = 0, right = 0;
        int maxCount = 0, result = 0;
        int[] freq = new int[26];

        while (right < s.length()) {
            freq[s.charAt(right) - 'A']++;
            maxCount = Math.max(maxCount, freq[s.charAt(right) - 'A']);

            while ((right - left + 1) - maxCount > k) {
                freq[s.charAt(left) - 'A']--;
                left++;
            }

            result = Math.max(result, right - left + 1);
            right++;
        }
        return result;
    }
}
