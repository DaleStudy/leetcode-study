class Solution {
public:
    int reverseBits(int n) {
        int r = 0;

        for (int i = 0; i <= 31; ++i)
        {
            int pot = 1 << i;
            if ((n & pot) != 0)
            {
                r |= (1 << (31 - i));
            }
        }

        return r;
    }
};
