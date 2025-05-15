/*
    풀이 :
        상하좌우 범위지정해서 이동하는 것이 아니라 n_rows, n_cols 길이만큼 이동으로 풀이
        col 방향으로 움직이면 이동할 row 감소, row 방향 움직이면 n_cols 1 감소
        row, col 한번씩 이동하면 direction *= -1로 방향을 바꿔준다

    matrix 크기 : M * N

    TC : O(M * N)
        matrix 전체 순환

    SC : O(1)
        리턴할 ans 제외하면 추가 메모리 사용은 상수 개수의 변수
*/

class Solution {
    public:
        vector<int> spiralOrder(vector<vector<int>>& matrix) {
            int n_rows = matrix.size();
            int n_cols = matrix[0].size();
            vector<int> ans;
    
            int row = 0, col = -1;
            int direction = 1;
    
            while (n_rows > 0 && n_cols > 0)
            {
                for (int i = 0; i < n_cols; i++)
                {
                    col += direction;
                    ans.push_back(matrix[row][col]);
                }
                n_rows--;
    
                for (int i = 0; i < n_rows; i++)
                {
                    row += direction;
                    ans.push_back(matrix[row][col]);
                }
                n_cols--;
    
                direction *= -1;
            }
            return ans;
        }
    };
