class Solution {
    public:
        vector<int> spiralOrder(vector<vector<int>>& matrix) {
            enum direction { R, D, L, U };
    
            enum direction dir = R;
            vector<int> result;
            int min_R = 0;
            int max_R = matrix.size() - 1;
            int min_C = 0;
            int max_C = matrix[0].size() - 1;
            int r = 0;
            int c = 0;
            int size = matrix.size() * matrix[0].size();
    
            while(result.size() < size){
                result.push_back(matrix[r][c]);
    
                switch(dir){
                    case R:
                        if(c == max_C){
                            dir = D;
                            min_R++;
                            r++;
                        }else
                            c++;
                        break;
                    case D:
                        if(r == max_R){
                            dir = L;
                            max_C--;
                            c--;
                        }else
                            r++;
                        break;
                    case L:
                        if(c == min_C){
                            dir = U;
                            max_R--;
                            r--;
                        }else
                            c--;
                        break;
                    case U:
                        if(r == min_R){
                            dir = R;
                            min_C++;
                            c++;
                        }else
                            r--;
                        break;
                }
            }
    
            return result;
        }
    };
