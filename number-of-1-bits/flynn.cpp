/**
 * For given integer N,
 * 
 * Time complexity: O(logN)
 * 
 * Space complexity: O(1)
 */

class Solution {
public:
    int hammingWeight(int n) {
        int res = 0;

        while (n) {
            if (n & 1) res++;
            n >>= 1;
        }

        return res;
    }
};