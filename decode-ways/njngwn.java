// Time Complexity: O(n), n: s.length()
// Space Complexity: O(n), n: s.length()
class Solution {
    public int numDecodings(String s) {
        if (s.length() == 0) {  // edge case
            return 0;
        }

        int length = s.length()+1;
        int[] cntArr = new int[length]; // using dynamic programming

        // check the case i == 0, i == 1 first
        cntArr[0] = 1;
        if (s.charAt(0) != '0') {
            cntArr[1] = 1;
        }

        for (int i = 2; i < length; ++i) {
            char ch = s.charAt(i-1);
            if (ch != '0') {   // check for 1-9
                cntArr[i] += cntArr[i-1];
            }

            // check for 10-26
            int num = (s.charAt(i-2)-'0') * 10 + (ch-'0');
            if (num >= 10 && num <= 26) {
                cntArr[i] += cntArr[i-2];
            }
        }

        return cntArr[length-1];
    }
}
