class Solution {
public:
    int getSum(int a, int b) {
        int ans = 0;
        int carry = 0;
        for(int i = 0; i < 32; i++) {
            ans = ans | ((1 << i) & (a ^ b ^ (carry << i)));
            carry = ((a >> i) & (b >> i) & 1) | (carry & ((a >> i) ^ (b >> i)));
            // cout << carry;
        }
        return ans;
    }
};
