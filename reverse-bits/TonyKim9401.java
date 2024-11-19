public class Solution {
    public int reverseBits(int n) {
        // time complexity O(1)
        // space complexity O(1)
        int output = 0;

        for (int i = 0; i < Integer.SIZE; i++) {
            output <<= 1;
            output += n & 1;
            n >>= 1;
        }
        return output;
    }
}
