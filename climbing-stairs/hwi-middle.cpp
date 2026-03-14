class Solution {
public:
    int climbStairs(int n) {
        int p = 1;
        int pp = 0;
        int cur = 0;
        for (int i = 0; i < n; ++i)
        {
            cur = p + pp;
            pp = p;
            p = cur;
        }

        return cur;
    }
};
