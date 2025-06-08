class Solution {
    public:
        void dfs(int prev, int r, int c, vector<vector<int>>& heights, vector<vector<bool>>& visit){
            if(r < 0 || c < 0 || r >= heights.size() || c >= heights[0].size() || visit[r][c] || heights[r][c] < prev)
                return;
            
            visit[r][c] = true;
    
            dfs(heights[r][c], r - 1, c, heights, visit);
            dfs(heights[r][c], r + 1, c, heights, visit);
            dfs(heights[r][c], r, c - 1, heights, visit);
            dfs(heights[r][c], r, c + 1, heights, visit);
        }
    
        vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
            vector<vector<int>> result;
            vector<vector<bool>> pacific(heights.size(), vector(heights[0].size(), false));
            vector<vector<bool>> atlantic(heights.size(), vector(heights[0].size(), false));
    
            for(int i = 0; i < heights.size(); i++){
                dfs(heights[i][0], i, 0, heights, pacific);
                dfs(heights[i][heights[0].size()-1], i, heights[0].size()-1, heights, atlantic);
            }
    
            for(int j = 0; j < heights[0].size(); j++){
                dfs(heights[0][j], 0, j, heights, pacific);
                dfs(heights[heights.size()-1][j], heights.size()-1, j, heights, atlantic);
            }
    
            for(int i = 0; i < heights.size(); i++){
                for(int j = 0; j < heights[0].size(); j++){
                    if(pacific[i][j] && atlantic[i][j]){
                        result.push_back({i, j});
                    }
                }
            }
    
            return result;
        }
    };
