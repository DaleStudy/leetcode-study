class Solution {
public:
    int getSum(int a, int b) {
        while(b) {
            int t = a ^ b;
            b = (a & b) << 1;
            a = t;
        }
        return a;
    }
};

