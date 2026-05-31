class Solution {
public:
    int getSum(int a, int b) {
        int res = 0;
        
        bool carry = false;
        for (int i = 0; i < 32; ++i)
        {
            int mask = 1 << i;
            bool bitA = a & mask;
            bool bitB = b & mask;
            bool sum = adder(bitA, bitB, carry);
            if (sum)
            {
                res |= mask;
            }
        }

        return res;
    }

    bool adder(bool a, bool b, bool& inout_carry)
    {
        bool axorb = a ^ b;
        bool sum = axorb ^ inout_carry;
        bool aandb = a & b;
        inout_carry = aandb | (axorb & inout_carry);
        return sum;
    }
};
