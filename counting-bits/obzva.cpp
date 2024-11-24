/**
 * Time complexity: O(N)
 * 
 * Space complexity: O(1)
 */

class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> res;
        res.push_back(0);

        int i = 1, j = 1;
        while (i <= n) {
            res.push_back(res[i - j] + 1);
            i++;
            if (i == j * 2) j *= 2;
        }

        return res;
    }
};
