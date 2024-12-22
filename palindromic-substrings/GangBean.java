class Solution {
    public int countSubstrings(String s) {
        /** 
            각 문자를 중간으로 갖는 palindrome 여부 체크
            + 두개의 문자를 중간으로 갖는 palindrome 여부 체크
        */
        int count = 0;
        int length = s.length();
        for (int i = 0; i < length; i++) { // O(N)
            int start = i;
            int end = i;
            while (0 <= start && end < length && start <= end && s.charAt(start) == s.charAt(end)) { // O(N)
                count++;
                start--;
                end++;
            }

            start = i;
            end = i + 1;
            while (0 <= start && end < length && start <= end && s.charAt(start) == s.charAt(end)) { // O(N)
                count++;
                start--;
                end++;
            }
        }

        return count; // O(N^2)
    }
}
