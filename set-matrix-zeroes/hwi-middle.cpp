// 풀이 1
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<pair<int, int>> v;
        v.reserve(m * n);

        // 0인 칸을 별도의 공간에 마킹
        for (int i = 0; i < m; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                if (matrix[i][j] == 0)
                {
                    v.push_back({i, j});
                }
            }
        }

        // 마킹이 끝난 후 해당 칸들을 확인하며 행과 열을 채움
        for (auto coord : v)
        {
            int x = coord.first;
            int y = coord.second;

            // 행
            for (int i = 0; i < n; ++i)
            {
                matrix[x][i] = 0;
            }

            // 열
            for (int i = 0; i < m; ++i)
            {
                matrix[i][y] = 0;
            }
        }
    }
};

// 풀이 2
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int r = matrix.size();
        int c = matrix[0].size();

        // 핵심 아이디어
        // - 각 행과 열에는 반드시 첫 번째 요소는 존재한다.
        // - 이를 활용하여 각 행과 열의 첫 번째 요소를 마킹용으로 사용한다.
        // - matrix[i][0]: i번째 행 전체를 0으로 만들어야 한다는 의미
        // - matrix[0][j]: j번째 열 전체를 0으로 만들어야 한다는 의미

        // 엣지 케이스
        // - matrix[0][0]: 0번째 행인지, 0번째 열인지 구분할 수 없음
        
        // 해결 방법
        // - matrix[0][0]은 0번째 행을 의미하도록 약속
        // - 0번째 열은 별도의 플래그를 둠

        bool isFirstColZero = false;
        for (int i = 0; i < r; ++i)
        {
            if (matrix[i][0] == 0) 
            {
                isFirstColZero = true;
            }

            for (int j = 1; j < c; ++j)
            {
                if (matrix[i][j] == 0)
                {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        for (int i = 1; i < r; ++i)
        {
            for (int j = 1; j < c; ++j)
            {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) 
                {
                    matrix[i][j] = 0;
                }
            }
        }

        if (matrix[0][0] == 0) 
        {
            for (int j = 0; j < c; j++) 
            {
                matrix[0][j] = 0;
            }
        }

        if (isFirstColZero) 
        {
            for (int i = 0; i < r; i++) 
            {
                matrix[i][0] = 0;
            }
        }
    }
};
