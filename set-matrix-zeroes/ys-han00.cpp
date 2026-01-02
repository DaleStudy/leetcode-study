// class Solution {
// public:
//     void setZeroes(vector<vector<int>>& matrix) {
//         vector<pair<int, int>> t;
//         for(int i = 0; i < matrix.size(); i++)
//             for(int j = 0; j < matrix[0].size(); j++)
//                 if(matrix[i][j] == 0)
//                     t.push_back({i, j});


//         for(pair<int, int> x : t) {
//             for(int k = 0; k < matrix.size(); k++)
//                 matrix[k][x.second] = 0;
//             for(int k = 0; k < matrix[0].size(); k++)
//                 matrix[x.first][k] = 0;
//         }

//         return;
//     }
// };

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        bool first_row = 0, first_col = 0;

        for(int i = 0; i < matrix.size(); i++)
            if(matrix[i][0] == 0)
                first_col = true;

        for(int i = 0; i < matrix[0].size(); i++)
            if(matrix[0][i] == 0)
                first_row = true;

        for(int i = 1; i < matrix.size(); i++) {
            for(int j = 1; j < matrix[0].size(); j++) {
                if(matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        for(int i = 1; i < matrix.size(); i++) 
            for(int j = 1; j < matrix[0].size(); j++)
                if(matrix[i][0] == 0 || matrix[0][j] == 0)
                    matrix[i][j] = 0;
        
        if(first_row)
            for(int k = 0; k < matrix[0].size(); k++)
                matrix[0][k] = 0;

        if(first_col)
            for(int k = 0; k < matrix.size(); k++)
                matrix[k][0] = 0;

        return;
    }
};

