// Time: O(n), Space: O(1)
class Solution {
public:
    int hammingWeight(int n) {
        int cnt = 0;
        while(n > 0) {
            cnt += n & 1;
            n = n >> 1;
        }

        return cnt;
    }
};
