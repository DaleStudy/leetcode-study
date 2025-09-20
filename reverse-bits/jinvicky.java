

public class Solution {
    public int reverseBits(int n) {
        int reversed = 0;

        for (int i = 0; i < 32; i++) {
            reversed <<= 1;

            int lsb_of_n = n & 1; // n이 홀수면 1, 짝수면 0을 반환

            reversed |= lsb_of_n;

            n >>= 1;
        }
        return reversed;
    }
}