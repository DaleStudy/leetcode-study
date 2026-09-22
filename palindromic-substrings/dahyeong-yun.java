/**
 * TC : O(n^2)
 *   - 문자열 길이 n 만큼 반복하고, 각 인덱스에서 n/2 만큼의 회문을 확인하므로 n * (n/2) => O(n^2)
 * SC : O(1)
 *   - 별도 유의미한 공간을 사용하지 않음 
 */
class Solution {
    public int countSubstrings(String s) {
        int len = s.length(), count = 0;

        for(int i = 0; i<len; i++) {
            int start = i, end = i;

            // 홀수 길이 회문 카운트
            while(
                start >= 0 && end < len && s.charAt(start) == s.charAt(end)
            ) {
                count++;
                start--;
                end++;
            }

            // 짝수 길이 회문 카운트
            start = i;
            end = i+1;
            while(
                start >= 0 && end < len && s.charAt(start) == s.charAt(end)
            ) {
                count++;
                start--;
                end++;
            }
        }

        return count;
    }
}
