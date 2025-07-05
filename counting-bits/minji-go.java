/**
 * <a href="https://leetcode.com/problems/counting-bits/">week14-1. counting-bits</a>
 * <li>Description: Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i</li>
 * <li>Topics: Dynamic Programming, Bit Manipulation</li>
 * <li>Time Complexity: O(N), Runtime 2ms       </li>
 * <li>Space Complexity: O(N), Memory 46.64MB   </li>
 */
class Solution {
    public int[] countBits(int n) {
        int[] count = new int[n + 1];

        int offset = 1;
        for (int i = 1; i <= n; i++) {
            if (i == offset * 2) offset *= 2;
            count[i] = count[i - offset] + 1;
        }

        return count;
    }
}
