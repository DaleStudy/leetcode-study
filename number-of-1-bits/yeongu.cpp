// Time complexity: O(n) 왜냐하면, while문
// Space complexity: O(1)

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
