/**
 * TC : O(n)
 *   - 문자열의 길이 n 만큼 반복하고 루프 안에서는 고정 길이를 반복하므로 O(n)
 * SC : O(1)
 *   - 26개 알파벳의 카운트를 위한 배열을 생성하므로 O(1)
 */
class Solution {
    public int characterReplacement(String s, int k) {
        int max = 0;

        int len = s.length();
        int deleteTarget = 0;
        int[] count = new int[26];
        for(int i=0; i<len; i++) {
            char c = s.charAt(i);
            count[c - 'A']++;

            
            int maxCountAlphabet = 0;
            int total = count[0];
            for(int j=1; j<26; j++) {
                total += count[j];    
                if(count[j] > count[maxCountAlphabet]) maxCountAlphabet = j;
            }

            if(total - count[maxCountAlphabet] <= k) {
                max = Math.max(max, total);
            } else {
                count[s.charAt(deleteTarget++) - 'A']--;
            }
        }

        return max;
    }
}
