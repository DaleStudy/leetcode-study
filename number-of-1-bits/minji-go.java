/**
 * <a href="https://leetcode.com/problems/number-of-1-bits/">week8-1.number-of-1-bits</a>
 * <li>Description: returns the number of set bits in its binary representation</li>
 * <li>Topics: Divide and Conquer, Bit Manipulation </li>
 * <li>Time Complexity: O(K), Runtime 0ms       </li>
 * <li>Space Complexity: O(1), Memory 40.57MB   </li>
 */

class Solution {
    public int hammingWeight(int n) {
        int count = 0;
        while (n != 0) {
            n = n & (n - 1);
            count++;
        }
        return count;
    }
}
