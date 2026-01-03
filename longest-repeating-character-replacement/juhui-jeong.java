/* 
 * 시간복잡도: O(n)
 * 공간복잡도: O(1)
*/
class Solution {
    public int characterReplacement(String s, int k) {
        int left = 0;
        int[] freq = new int[26];
        int maxFreq = 0;
        int ans = 0;

        for (int right = 0; right < s.length(); right++) {
            int rIdx = s.charAt(right) - 'A';
            freq[rIdx]++;
            maxFreq = Math.max(maxFreq, freq[rIdx]);

            while((right - left + 1) - maxFreq > k) {
                int lIdx = s.charAt(left) - 'A';
                freq[lIdx]--;
                left++;
            }
            ans = Math.max(ans, right - left + 1);
        }
        return ans;
    }
}