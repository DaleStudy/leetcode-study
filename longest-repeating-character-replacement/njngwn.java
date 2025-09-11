// Time Complexity: O(n), n: s.length()
// Space Complexity: O(1)
class Solution {
    public int characterReplacement(String s, int k) {
        int[] charFreqArr = new int[26]; // s consists of only uppercase English letters
        int maxFreq = 0;
        int maxLength = 0;

        for (int left = 0, right = 0; right < s.length(); right++) {
            char letter = s.charAt(right);
            int letterIdx = letter-'A';

            charFreqArr[letterIdx]++;
            maxFreq = Math.max(maxFreq, charFreqArr[letterIdx]);

            // when left idx moves rightward? -> k + maxFreq < size of sliding window
            // here, we don't neet to recalculate maxFreq because the point is to calculate 'best' maxFreq
            if (maxFreq + k < right-left+1) {
                char leftChar = s.charAt(left);
                charFreqArr[leftChar-'A']--;
                left++;
            }

            maxLength = Math.max(maxLength, right-left+1);
        }

        return maxLength;
    }
}

// AABABBA, k=1, maxFreq=1, maxLength=1
// l
// r

// AABABBA, k=1, maxFreq=2, maxLength=2
// lr

// AABABBA, k=1, maxFreq=2, maxLength=3
// l r

// AABABBA, k=1, maxFreq=3, maxLength=4
// l  r

// AABABBA, k=1, maxFreq=3, maxLength=4 ==> fail
// l   r

// AABABBA, k=1, maxFreq=3
//  l   r
