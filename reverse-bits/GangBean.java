public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        /**
        1. understanding
        - return the reversed 32 bit input num
        2. strategy
        - assign stack
        - iterate until stack.size is 32
        - push value % 2, and value /= 2
        3. complexity
        - time: O(1)
        - space: O(1)
        */
        int reversed = 0;
        for (int i = 0; i < 32; i++) {
            reversed <<= 1;
            reversed |= n & 1;
            n >>= 1;
        }
        return reversed;
    }
}

