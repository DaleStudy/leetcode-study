/**
 * 풀이
 * - matrix 전체를 탐색하다가 값이 0인 좌표를 찾으면
 *   그 좌표의 첫번째 열, 첫번째 행 좌표에 표시를 합니다
 *   if matrix[r][c] == 0
 *     matrix[r][0] = 0
 *     matrix[0][c] = 0
 * - 만약 해당 좌표가 첫번째 행이거나 첫번째 열이라면 따로 기록해둡니다
 * - 첫번째 완전탐색을 마친 후엔 matrix의 첫번째 행, 열을 보고 문제에서 요구하는 바를 수행합니다
 * 
 * Big O
 * - M: matrix의 행 개수
 * - N: matrix의 열 개수
 * 
 * - Time complexity: O(MN)
 * - Space complexity: O(1)
 *     
 */

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();

        bool first_row = false;
        bool first_col = false;

        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (!matrix[r][c]) {
                    if (!r) first_row = true;
                    if (!c) first_col = true;
                    matrix[r][0] = 0;
                    matrix[0][c] = 0;
                }
            }
        }

        for (int r = 1; r < m; ++r) {
            if (!matrix[r][0]) {
                for (int c = 1; c < n; ++c) matrix[r][c] = 0;
            }
        }

        for (int c = 1; c < n; ++c) {
            if (!matrix[0][c]) {
                for (int r = 1; r < m; ++r) matrix[r][c] = 0;
            }
        }

        if (first_row) {
            for (int c = 0; c < n; ++c) matrix[0][c] = 0;
        }

        if (first_col) {
            for (int r = 0; r < m; ++r) matrix[r][0] = 0;
        }
    }
};
