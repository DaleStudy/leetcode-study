import java.util.*;

// TC: O(n)
// SC: O(1)
class Solution {
    public int characterReplacement(String s, int k) {
        int[] counts = new int[26];
        int left = 0;

        for (int right = 0; right < s.length(); right++) {
            counts[toAlphabetIndex(s.charAt(right))]++;

            int windowLength = right - left + 1;
            int mostFreq = Arrays.stream(counts).max().getAsInt();
            //바꿀 대상이 k 횟수보다 크면, left을 옮김
            if (windowLength - mostFreq > k) {
                counts[toAlphabetIndex(s.charAt(left))]--;
                left++;
            }
        }

        return s.length() - left;
    }

    private int toAlphabetIndex(char c) {
        return c - 'A';
    }

}
