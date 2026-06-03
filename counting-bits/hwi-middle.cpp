class Solution {
public:
    vector<int> countBits(int n) {
        // i & (i - 1)은 가장 오른쪽 비트 1을 지운다는 성질을 이용
        vector<int> ans(n + 1); // ans[0]은 0으로 초기화
        for (int i = 1; i <= n; ++i)
        {
            ans[i] = ans[i & (i - 1)] + 1;
        }

        return ans;
    }
};
