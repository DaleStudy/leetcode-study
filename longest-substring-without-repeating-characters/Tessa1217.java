/**
 * 문자열 s가 주어질 때 중복 문자가 없는 가장 긴 문자열 길이를 반환하세요.
 * */
class Solution {
    // 시간복잡도: O(n)
    public int lengthOfLongestSubstring(String s) {

        int maxLength = 0;

        int left = 0;
        int right = 0;

        // 알파벳 (대소문자), 숫자, 특수문자, 공백
        boolean[] visited = new boolean[128];

        while (right < s.length()) {
            while (visited[s.charAt(right)]) {
                visited[s.charAt(left)] = false;
                left++;
            }
            visited[s.charAt(right)] = true;
            maxLength = Math.max(right - left + 1, maxLength);
            right++;
        }

        return maxLength;
    }
}

