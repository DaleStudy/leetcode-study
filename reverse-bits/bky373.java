/**
 * https://leetcode.com/problems/reverse-bits/
 *
 * time: O(1)
 * space: O(1)
 */
public class Solution {

    public int reverseBits(int n) {
        int ans = 0;
        for (int i = 0; i < 32; i++) {
            ans = ans << 1 | n & 1;
            n >>= 1;
        }
        return ans;
    }
}
