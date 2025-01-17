/*
runtime 0 ms, beats 100.00%
memory 41.47 MB, beats 90.14%

time complexity: O(1)
space complexity: O(1)

i번째 bit를 구하고, 이를 ans(초기값 0)의 31-i번째 자리에 bitwise-OR 연산을 하여, bit 위치를 reverse 했습니다.
*/

public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int x = 1;
        int ans = 0;
        for (int i = 0; i < 32; i++) {
            int bit = (x & n) >>> i;
            bit <<= (31 - i);
            ans |= bit;
            x <<= 1;
        }
        return ans;
    }
}
