// Time: O(N), Space: O(N)
class Solution {
public:
    int numDecodings(string s) {
        int n = s.size();
        unordered_map<int, int> cache;

        auto canTakeTwo = [&](int i) {
            if (i + 1 >= n) return false;
            string two = s.substr(i, 2);
            return "10" <= two && two <= "26";
        };

        auto countFrom = [&](this auto&& self, int i) -> int {
            if (i == n) return 1;
            if (s[i] == '0') return 0;
            if (cache.count(i)) return cache[i];

            int ways = self(i + 1);
            if (canTakeTwo(i)) {
                ways += self(i + 2);
            }
            return cache[i] = ways;
        };

        return countFrom(0);
    }
};
