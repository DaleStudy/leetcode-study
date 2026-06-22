class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();

        int top = 0;
        int bottom = m - 1;
        int left = 0;
        int right = n - 1;

        vector<int> v;
        v.reserve(m * n);

        while(top <= bottom && left <= right)
        {
            // 오른쪽으로 이동
            for (int i = left; i <= right; ++i)
            {
                v.push_back(matrix[top][i]);
            }
            top++;

            // 아래쪽으로 이동
            for (int i = top; i <= bottom; ++i)
            {
                v.push_back(matrix[i][right]);
            }
            right--;

            // 왼쪽으로 이동
            if (top <= bottom)
            {
                for (int i = right; i >= left; --i)
                {
                    v.push_back(matrix[bottom][i]);
                }
                bottom--;
            }

            // 위쪽으로 이동
            if (left <= right)
            {
                for (int i = bottom; i >= top; --i)
                {
                    v.push_back(matrix[i][left]);
                }
                left++;
            }
        }

        return v;
    }
};
