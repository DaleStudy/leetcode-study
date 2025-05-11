class Solution {
    public:
        void setZeroes(vector<vector<int>>& matrix) {
            int rows = matrix.size();
            int cols = matrix[0].size();
    
            bool firstRowZero = false;
            bool firstColZero = false;
    
            for(int j = 0; j < cols; j++){
                if(matrix[0][j] == 0)
                    firstRowZero = true;
            }
    
            for(int i = 0; i < rows; i++){
                if(matrix[i][0] == 0)
                    firstColZero = true;
            }
    
            for(int i = 1; i < rows; i++){
                for(int j = 1; j < cols; j++){
                    if(matrix[i][j] == 0){
                        matrix[i][0] = 0;
                        matrix[0][j] = 0;
                    }
                }
            }
    
            for(int i = 1; i < matrix.size(); i++){
                for(int j = 1; j < matrix[0].size(); j++){
                    if(matrix[0][j] == 0 || matrix[i][0] == 0)
                        matrix[i][j] = 0;
                }        
            }
    
            if(firstRowZero){
                for(int j = 0; j < cols; j++)
                    matrix[0][j] = 0;
            }
    
            if(firstColZero){
                for(int i = 0; i < rows; i++)
                    matrix[i][0] = 0;
            }
        }
    };
