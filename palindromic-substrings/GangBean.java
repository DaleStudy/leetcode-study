class Solution {
    public int countSubstrings(String s) {
        /** 
        1. understanding
        - find the number of palindromic substrings
        2. strategy
        - iterate over each character, count below substrings
        - First, start with same position, move left and right directions each, until two charactes are not same.
        - Second, start with i and i + 1 position, move left and right directions until two chracters are not same.
        3. complexity
        - time: O(N^2)
        - space: O(1)
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

