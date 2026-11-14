// Time Complexity: O(n)
// Space Complexity: O(n), including memoization and recursion stack

class Solution {
public:

    int rob(vector<int>& nums) {
        int N = nums.size();
        vector<int> cache(N, -1);

        function<int(int)> recur = [&](int cur) -> int {
            if (cur >= N) return 0;
            if (cache[cur] != -1) return cache[cur];

            int a = recur(cur + 1);
            int b = recur(cur + 2) + nums[cur];

            return cache[cur] = max(a, b);
        };

        return recur(0);
    }
};
