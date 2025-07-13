class Solution {

    // 시간복잡도: O(N^2)
    public String longestPalindrome(String s) {

        // 회문 구성 불가 경우
        if (s == null || s.length() < 1) {
            return "";
        }

        String result = "";

        for (int i = 0; i < s.length(); i++) {
            String odd = palindrome(s, i, i);
            String even = palindrome(s, i, i + 1);

            if (odd.length() > result.length()) {
                result = odd;
            }
            if (even.length() > result.length()) {
                result = even;
            }

        }

        return result;

    }

    private String palindrome(String s, int left, int right) {

        // 중앙을 기준으로 좌우 회문 여부 검사        
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }

        return s.substring(left + 1, right);
    }

}

