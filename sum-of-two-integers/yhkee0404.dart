class Solution {
  int getSum(int a, int b) {
    int ans = 0;
    // for (int i = 0, carry = 0, ai, bi, u = 1; i != 64 && (carry | a | b) != 0; i++, a >>>= 1, b >>>= 1, u <<= 1) { // significand 53 bits but u has only 1 bit
    for (int i = 0, carry = 0, ai, bi, u = 1; i != 32 && (carry | a | b) != 0; i++, a >>= 1, b >>= 1, u <<= 1) {
        ai = a & 1;
        bi = b & 1;
        if ((ai & bi) == 1) {
            if (carry == 1) {
                ans |= u;
            }
            carry = 1;
        } else if ((ai ^ bi) == 1) {
            if (carry == 0) {
                ans |= u;
            }
        } else {
            if (carry == 1) {
                ans |= u;
            }
            carry = 0;
        }
    }
    // return ans;
    return (ans & 0x80000000) != 0 ? ans | ~ 0xFFFFFFFF : ans;
  }
}
