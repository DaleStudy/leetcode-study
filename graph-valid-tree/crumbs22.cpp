/*
	valid tree 조건
	1. 사이클이 없어야한다
	2. 모든 각 노드들은 적어도 하나의 다른 노드와 연결되어 있어야 한다

	인접 리스트 형식으로 무방향 간선 정보를 저장하고,
	dfs 재귀 탐색으로 방문 체크 후 자식 노드를 재귀적으로 방문하면서 사이클 판단
*/

class Solution {
	public:
		/**
		 * @param n: An integer
		 * @param edges: a list of undirected edges
		 * @return: true if it's a valid tree, or false
		 */
		bool validTree(int n, vector<vector<int>> &edges) {
			if (edges.size() != n - 1)
				return false;
	
			// 인접한 노드들을 요소로 가지는 adj 배열 생성
			vector<vector<int>> adj(n);
	
			for (auto edge : edges) {
				int u = edge[0];
				int v = edge[1];
				adj[u].push_back(v);
				adj[v].push_back(u);
			}
	
			// 방문 기록
			vector<bool> visited(n, false);
			if (!dfs(0, -1, adj, visited))
				return false;
			
			// 모든 노드가 방문되었는지 (연결되는지) 확인
			for (bool v : visited) {
				if (!v)
					return false;
			}
			return true;
		}
	
		bool dfs(int node, int parent, vector<vector<int>>& adj, vector<bool> visited) {
			visited[node] = true;
	
			for (int neighbor : adj[node]) {
				if (neighbor == parent)
					continue ; // 바로 이전 노드는 무시(왕복 방지)
				if (visited[neighbor])
					return false; // 사이클 탐지
				if (!dfs(neighbor, node, adj, visited))
					return false;
			}
			return true;
		}
	};
