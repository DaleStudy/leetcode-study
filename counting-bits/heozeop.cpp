// Time Complexity: O(n^2)
// Spatial Complexity: O(n)

class Solution {
private:
    int count1(int n) {
        int ans = 0;
  
        while(n) {
            if (n % 2) {
                ++ans;
            }

            n /= 2;
        }

        return ans;
    }

public:
    vector<int> countBits(int n) {
        vector<int> ans(n + 1);

        for(int i = 0; i <= n; ++i) {
            ans[i] = this->count1(i);
        }

        return ans;
    }
};

