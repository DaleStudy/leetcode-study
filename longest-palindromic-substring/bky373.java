class Solution {

    /*
     * Approach 1.
     * time: O(n^3)
     * space: O(1)
     */
    public String longestPalindrome1(String s) {
        String longest = "";
        for (int i = 0; i < s.length(); i++) {
            for (int j = i; j < s.length(); j++) {
                String ss = s.substring(i, j + 1);
                if (isPalindrome(ss)) {
                    if (ss.length() > longest.length()) {
                        longest = ss;
                    }
                }
            }
        }
        return longest;
    }

    // Approach 1.
    private boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    /*
     * Approach 2-1.
     * time: 시간 복잡도는 평균적으로 O(n)이고, palindrome 의 길이가 n 에 가까워지면 시간 복잡도 역시 O(n^2) 에 가까워 진다.
     * space: O(1)
     */
    class Solution {

        public String longestPalindrome(String s) {
            int maxStart = 0;
            int maxEnd = 0;

            for (int i = 0; i < s.length(); i++) {
                int start = i;
                int end = i;
                while (0 <= start && end < s.length() && s.charAt(start) == s.charAt(end)) {
                    if (maxEnd - maxStart < end - start) {
                        maxStart = start;
                        maxEnd = end;
                    }
                    start--;
                    end++;
                }

                start = i;
                end = i + 1;
                while (0 <= start && end < s.length() && s.charAt(start) == s.charAt(end)) {
                    if (maxEnd - maxStart < end - start) {
                        maxStart = start;
                        maxEnd = end;
                    }
                    start--;
                    end++;
                }
            }
            return s.substring(maxStart, maxEnd + 1);
        }
    }

    /*
     * Approach 2-2.
     * time: 시간 복잡도는 평균적으로 O(n)이고, palindrome 의 길이가 n 에 가까워지면 시간 복잡도 역시 O(n^2) 에 가까워 진다.
     * space: O(1)
     */
    class Solution {
        int maxStart = 0;
        int maxEnd = 0;

        public String longestPalindrome(String s) {
            for (int i = 0; i < s.length(); i++) {
                calculateMaxLength(i, i, s);
                calculateMaxLength(i, i+1, s);
            }
            return s.substring(maxStart, maxEnd + 1);
        }

        public void calculateMaxLength(int start, int end, String s){
            while (start >= 0 && end < s.length() && s.charAt(start) == s.charAt(end)) {
                if (this.maxEnd - this.maxStart < end - start) {
                    this.maxStart = start;
                    this.maxEnd = end;
                }
                start--;
                end++;
            }
        }

    }
}
