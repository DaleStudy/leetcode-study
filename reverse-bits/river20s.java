public class Solution {
    /* T.C = O(1)
     * S.C = O(1)
     */
    public int reverseBits(int n) {
        // Set the output to 0
        int output = 0;
        // Repeat 32 times 
        for (int i = 0; i < 32; i++) {
            // Shift the output value one space to the left to make room for the new bit
            output <<= 1;
            // '&' operation to get the rightmost bit and add it to the output 
            output = output | (n & 1);
            // Discard the rightmost bit of the 'n'
            n = n >> 1;
        }

        return output;
        
    }
}

