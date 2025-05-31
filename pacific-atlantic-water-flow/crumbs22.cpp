class Solution {
	public:
	
		vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
			int m = heights.size();
			if (m == 0)
				return {};
			int n = heights[0].size();
			if (n == 0)
				return {};
			
			vector<vector<bool>> reachP(m, vector<bool>(n, false));
			vector<vector<bool>> reachA(m, vector<bool>(n, false));
			queue<pair<int, int>> qP, qA;
	
	
			// Pacific 경계 초기화
			for (int i = 0; i < m; i++) {
				reachP[i][0] = true;
				qP.emplace(i, 0); // Pacific 경계에서 시작할 좌표로 큐에 등록. 이후 이 좌표들은 BFS의 출발점이 됨
			}
			for (int j = 0; j < n; j++) {
				reachP[0][j] = true;
				qP.emplace(0, j);
			}
	
			// Atlantic 경계 초기화
			for (int i = 0; i < m; i++) {
				reachA[i][n - 1] = true;
				qA.emplace(i, n - 1);
			}
			for (int j = 0; j < n; j++) {
				reachA[m - 1][j] = true;
				qA.emplace(m - 1, j);
			}
	
			// 각 경계에 대한 bfs
			bfs(heights, qP, reachP);
			bfs(heights, qA, reachA);
	
			// 두 경계에 모두 도달 가능한 셀 수집
			vector<vector<int>> ans;
			for (int i = 0; i < m; i++) {
				for (int j = 0; j < n; j++) {
					if (reachP[i][j] && reachA[i][j]) {
						ans.push_back({i, j});
					}
				}
			}
			return (ans);
		}
	
		void bfs(const vector<vector<int>>& h, queue<pair<int, int>>& q, vector<vector<bool>>& reach) {
			int m = h.size();
			int n = h[0].size();
			int dr[4] = {1, -1, 0, 0};
			int dc[4] = {0, 0, 1, -1};
	
			while (!q.empty()) {
				auto [r,c] = q.front();
				q.pop();
				for (int d = 0; d < 4; d++) {
					int nr = r + dr[d];
					int nc = c + dc[d];
	
					if (nr < 0 || nr >= m || nc < 0 || nc >= n)
						continue ;
					if (reach[nr][nc])
						continue ;
					if (h[nr][nc] < h[r][c])
						continue ;
					reach[nr][nc] = true;
					q.emplace(nr, nc);
				}
			}
		}
	};
