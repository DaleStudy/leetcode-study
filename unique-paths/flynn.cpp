/**
 * 풀이
 * - 조합 공식을 사용하면 overflow 및 시간초과를 일으킬 수 있습니다
 * - 모든 좌표에 대해 uniquePaths를 계산하는 방식을 사용합니다
 * - 특정 좌표의 uniquePaths를 계산하기 위해서는 두 행만 필요하기 때문에 길이 m의 배열 두 개를 이용합니다
 * 
 * Big O
 * - Time complexity: O(MN)
 * - Space compexity: O(N)
 */

class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> row1;
        vector<int> row2;

        for (int i = 0; i < n; ++i) row1.push_back(1);
        row2.push_back(1);
        for (int i = 1; i < n; ++i) row2.push_back(0);

        for (int j = 1; j < m; ++j) {
            for (int i = 1; i < n; ++i) row2[i] = row1[i] + row2[i - 1];
            swap(row1, row2);
            row2[0] = 1;
            for (int i = 1; i < n; ++i) row2[i] = 0;
        }

        return row1[n - 1];
    }
};
