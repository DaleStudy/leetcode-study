class Solution {
    public:
        void search(int r, int c, vector<vector<char>>& grid){
            if(r < 0 || c < 0 || r >= grid.size() || c >= grid[r].size() || grid[r][c] == '0')
                return;
            
            grid[r][c] = '0';
    
            search(r-1, c, grid);
            search(r+1, c, grid);
            search(r, c-1, grid);
            search(r, c+1, grid);
        }
    
        int numIslands(vector<vector<char>>& grid) {
            int cnt = 0;
    
            for(int i = 0; i < grid.size(); i++){
                for(int j = 0; j < grid[i].size(); j++){
                    if(grid[i][j] == '1'){
                        search(i, j, grid);
                        cnt++;
                    }
                }
            }
    
            return cnt;
        }
    };