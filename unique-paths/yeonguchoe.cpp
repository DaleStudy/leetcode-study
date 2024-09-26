class Solution {
public:
    int combination(int n, int r) {
        int k = n - r > r ? r : n - r;
        unsigned long long result = 1;
        for (int i = 0; i < k; i++) {
            result = result * (n - i) / (i + 1);
        }
        return result;
    }
    int uniquePaths(int m, int n) { return combination(m - 1 + n - 1, m - 1); }
    // 시간 복잡도: O(min(m,n))
    // 공간 복잡도: O(1)
};
