class Solution {
    public int numDecodings(String s) {
        /**
            1. understanding
            - number to upper case alphabet mapping code: 1 -> A, ... 26 -> Z
            - many ways to decode each input string
            - also there can be no way to decode input string.
            - answer fits in 32-bit integer.

            2. example
            - 12: (1, 2), (12)
            - 226: (2, 2, 6), (2, 26), (22, 6)
            - 06: (0, x)

            3. strategy
            - iterate in reverse order,
            - at index k, dp[k] means the count of decode ways till that index.
            - dp[k-1] = 0 if num[k] == 0
            - dp[k-1] = dp[k] + dp[k+1] if 1<= nums[k-1:k] < 27
            - dp[k-1] = dp[k]
            - dp[n] = 1 -> assume that first empty input can be decoded in 1 way.

            4. complexity
            - time: O(N)
            - space: O(1)
        */
        int prev = 1;
        int current = 1;
        for (int i = s.length()-1; i >= 0; i--) { // O(1)
            if (s.charAt(i) == '0') {
                int tmp = current;
                current = 0;
                prev = tmp;
            } else if ( (i+1) < s.length() && Integer.parseInt(s.substring(i, i+2)) < 27) {
                int tmp = current;
                current = prev + current;
                prev = tmp;
            } else {
                prev = current;
            }
        }
        return current;
    }
}

