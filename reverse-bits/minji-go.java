/*
    Problem: https://leetcode.com/problems/reverse-bits/
    Description: Reverse bits of a given 32 bits unsigned integer
    Topics: Divide and Conquer, Bit Manipulation
    Time Complexity: O(1), Runtime 1ms
    Space Complexity: O(1), Memory 41.72MB
*/
public class Solution {
    public int reverseBits(int n) {
        long unsignedNum = n > 0 ? n : n + 2 * (long) Math.pow(2,31); //= Integer.toUnsignedLong()

        int reversedNum = 0;
        for(int i=31; i>=0; i--){
            if(unsignedNum % 2 == 1) reversedNum += (long) Math.pow(2,i); //= (1<<i)
            unsignedNum/=2;
        }
        return reversedNum;
    }
}
