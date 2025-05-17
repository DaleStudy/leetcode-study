/*
    풀이 :
        row0과 col0 을 해당 줄이 0이 되는지 지표로 사용해서 공간복잡도 O(1)을 달성할 것이다
        
        1. row0과 col0 중에 0이 존재하는지 미리 확인하고 변수에 저장

        2. matrix를 순회(첫행, 첫열 제외)하면서 0인 칸을 만나면 해당 정보를 첫행, 첫열에 저장

        3. 저장된 정보를 바탕으로 matrix 업데이트

        4. 변수에 담았던 첫행, 첫열에 0이 존재하는가 바탕으로 업데이트

    matrix 크기 : M * N

    TC : O(M * N)

    SC : O(1)
*/

#include <vector>
using namespace std;

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        bool firstRowZero = false, firstColZero = false;

        int nRows = matrix.size();
        int nCols = matrix[0].size();

        for (int i = 0; i < nRows; i++)
            if (matrix[i][0] == 0)
                firstColZero = true;

        for (int j = 0; j < nCols; j++) 
            if (matrix[0][j] == 0)
                firstRowZero = true;

        for (int i = 1; i <nRows; i++) {
            for (int j = 1; j < nCols; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        for (int i = 1; i < nRows; i++) {
            for (int j = 1; j < nCols; j++)
                if (matrix[i][0] == 0 || matrix[0][j] == 0)
                    matrix[i][j] = 0;
        }

        if (firstRowZero) {
            for (int i = 0; i < nCols; i++)
                matrix[0][i] = 0;
        }

        if (firstColZero) {
            for (int i = 0; i < nRows; i++)
                matrix[i][0] = 0;
        }
    }
};
