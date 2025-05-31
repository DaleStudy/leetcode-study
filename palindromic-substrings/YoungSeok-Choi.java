// tc O(n^3)... 입력값이 조금만 켜졌으면 바로 TLE가 발생했을 것..
class Solution {
    public int countSubstrings(String s) {
        int pCnt = 0;

        for (int i = 1; i <= s.length(); i++) {
            String window = s.substring(0, i);
            String prev = window;

            if (isPalindrome(window))
                pCnt++;

            for (int j = window.length(); j < s.length(); j++) {
                prev = new StringBuilder(prev).append(s.charAt(j)).substring(1);
                if (isPalindrome(prev)) {
                    pCnt++;
                }
            }
        }

        return pCnt;
    }

    public boolean isPalindrome(String p) {

        if (p.length() <= 0)
            return false;

        int start = 0;
        int end = p.length() - 1;

        while (start <= end) {
            if (p.charAt(start) != p.charAt(end)) {
                return false;
            }

            start++;
            end--;
        }

        return true;
    }
}
