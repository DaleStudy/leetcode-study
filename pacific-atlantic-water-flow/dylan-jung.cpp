class Solution {
public:
    int m, n;
    int pside[200][200];
    int aside[200][200];

    void aflow(vector<vector<int>>& heights, int a, int b) {
        int& val = aside[a][b];
        if(val == 1) return;
        int dx[4] = {1, -1, 0, 0};
        int dy[4] = {0, 0, 1, -1};
        val = 1;
        for(int i = 0; i < 4; i++) {
            int na = a+dx[i];
            int nb = b+dy[i];
            if(!(0 <= na && na < m && 0 <= nb && nb < n)) continue;
            if(heights[na][nb] >= heights[a][b])
                aflow(heights, na, nb);
        }
    }

    void pflow(vector<vector<int>>& heights, int a, int b) {
        int& val = pside[a][b];
        if(val == 1) return;
        int dx[4] = {1, -1, 0, 0};
        int dy[4] = {0, 0, 1, -1};
        val = 1;
        int ans = 0;
        for(int i = 0; i < 4; i++) {
            int na = a+dx[i];
            int nb = b+dy[i];
            if(!(0 <= na && na < m && 0 <= nb && nb < n)) continue;
            if(heights[na][nb] >= heights[a][b])
                pflow(heights, na, nb);
        }
    }

    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        m = heights.size();
        n = heights[0].size();
        fill(&pside[0][0], &pside[0][0]+200*200, 0);
        fill(&aside[0][0], &aside[0][0]+200*200, 0);
        vector<vector<int>> ans;

        for(int i = 0; i < m; i++) aflow(heights, i, n-1);
        for(int i = 0; i < n; i++) aflow(heights, m-1, i);
        for(int i = 0; i < m; i++) pflow(heights, i, 0);
        for(int i = 0; i < n; i++) pflow(heights, 0, i);

        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                // cout << pside[i][j] << " ";
                if (pside[i][j] && aside[i][j]) {
                    ans.push_back({i, j});
                }
            }
            // cout << "\n";
        }
        return ans;
    }
};
