class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> result(n + 1, 0);

        for(int i = 0; i <= n; i++){
            result[i] = result[i >> 1] + (i & 1);
        }

        return result;
    }
};
