// class Solution {
// public:
//     int reverseBits(int n) {
//         string bits = "";

//         while(n) {
//             bits += (n % 2) + '0';
//             n /= 2;
//         }

//         while(bits.size() < 32)
//             bits += '0';

//         int ans = 0, d = 1;
//         for(int i = 31; i >= 0; i--) {
//             ans += d * (bits[i] - '0');
//             d <<= 1;
//         }

//         return ans;
//     }
// };

class Solution {
public:
    int reverseBits(int n) {
        int ans = 0;
        for(int i = 0; i < 32; i++) {
            ans <<= 1;
            ans |= (n & 1);
            n >>= 1; 
        }
        return ans;
    }
};

