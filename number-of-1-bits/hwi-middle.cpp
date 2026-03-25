class Solution {
public:
    int hammingWeight(int n) {
        // 아주 간편한 풀이가 있지만...
        // return __builtin_popcount(n);

        // 직접 해보기
        int cnt = 0;
        for (unsigned int i = 1 << 31; i > 0; i /= 2)
        {
            if ((n & i) != 0)
            {
                cnt++;
            }
        }

        return cnt;
    }
};
