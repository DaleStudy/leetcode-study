class Solution {
    public int hammingWeight(int n) {
        int count = 0; 

        while (n != 0) {
            if ((n & 1) == 1) {
                count++; 
            }
            n = n >>> 1;
        }

        return count; 
    }
}

/**
Time: O(1) – max 32 iterations (fixed bit size)
Space: O(1)

How it works: Shift each bit → Check → Count → Shift again
    1. Shift each bit of n to the right
    2. Check if the last bit is 1 using n & 1
    3. If it is, increment the count
    4. Shift n to the right using n = n >>> 1

Learned:
    (n & 1) isolates the least significant bit (LSB) to check if it’s 1
    >>  : Arithmetic shift (fills in sign bit, so infinite loop for negatives)
    >>> : Logical shift (always fills with 0, safe for negatives)
    Java evaluates == before &, so use parentheses to control the order
 */
