class Solution {
public:
    int uniquePaths(int m, int n) {
        // 결과 구하기: C(m + n - 2, m - 1)

        int k = min(m - 1, n - 1); // C(n, k) = C(n, n - k)
        return combination(m + n - 2, k);
    }

    int combination(int n, int k)
    {
        long long res = 1;
        for (int i = 1; i <= k; ++i)
        {
            res = res * (n - i + 1) / i;
        }

        return res;
    }
};
