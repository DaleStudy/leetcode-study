/**
 * <a href="https://leetcode.com/problems/sum-of-two-integers/">week9-4. sum-of-two-integers</a>
 * <li>Description: Given two integers a and b, return the sum of the two integers without using the operators + and -.</li>
 * <li>Topics: Math, Bit Manipulation           </li>
 * <li>Time Complexity: O(1), Runtime 0ms       </li>
 * <li>Space Complexity: O(1), Memory 40.51MB   </li>
 */
class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            int tmp = (a & b) << 1;
            a = (a ^ b);
            b = tmp;
        }
        return a;
    }
}
