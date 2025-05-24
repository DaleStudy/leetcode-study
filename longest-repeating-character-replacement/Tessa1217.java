/**
 * 문자열 s와 정수 k가 주어진다. 
 * 문자열 내 아무 문자나 대문자 영문자로 변경할 수 있으며 해당 연산을 k번까지 할 수 있을 때,
 * 같은 문자를 포함하는 가장 긴 부분 수열을 반환하세요.
 */
class Solution {

    // 시간복잡도: O(n)
    public int characterReplacement(String s, int k) {

        int[] chars = new int[26];
        int left = 0;
        int maxLength = 0;
        int maxCnt = 0;

        for (int right = 0; right < s.length(); right++) {
            int charIdx = s.charAt(right) - 'A';
            chars[charIdx]++;
            // 현재 윈도우 내에서 가장 많이 등장하는 문자의 개수
            maxCnt = Math.max(chars[charIdx], maxCnt);

            // window size - max cnt > k (window 사이즈 조정)
            while (right - left + 1 - maxCnt > k) {
                chars[s.charAt(left) - 'A']--;
                left++;
            }

            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;

    }
}

