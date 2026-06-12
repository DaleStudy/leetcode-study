class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        // transpose 후 뒤집으면 90도 회전
        for (int i = 0; i < n; ++i)
        {
            for (int j = i; j < n; ++j)
            {
                swap(matrix[i][j], matrix[j][i]);
            }
        }

        for (int i = 0; i < n; ++i)
        {
            reverse(matrix[i].begin(), matrix[i].end());
        }
    }
};
