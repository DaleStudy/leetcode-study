class Solution {
public:
    int hammingWeight(int n) {
        int cnt = 0;
        while(n>0){
            int val = n%2;
            cnt+=val;
            n/=2;
        }
        return cnt;
    }
};
