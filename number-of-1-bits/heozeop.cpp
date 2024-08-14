class Solution {
public:
    int hammingWeight(int n) {
        int numberOf1Bit = 0;
        while(n) {
            if(n % 2) {
                numberOf1Bit += 1;
            }

            n = n >> 1;
        }

        return numberOf1Bit;
    }
};

