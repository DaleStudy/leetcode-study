/*
풀이
- valid tree인지 판별하는 문제입니다
  주어진 input이 valid tree이려면,
  1. cycle이 없어야 합니다 (cycle이 있는 경우: [[0, 1], [1, 2], [2, 0]])
  2. 모든 node가 연결되어 있어야 합니다 (모든 node가 연결되지 않은 경우: [[0, 1], [2, 3]])
- dfs 방식의 함수를 재귀 호출하여 풀이할 수 있습니다
Big O
- N: n
- E: 주어진 배열 edges의 크기
- Time complexity: O(N)
  - 모든 node를 최대 1번씩 탐색합니다
- Space complexity: O(E + N)
  - visited의 크기는 N에 비례하여 증가합니다 -> O(N)
  - adj의 크기는 E에 비례하여 증가합니다 -> O(E)
  - dfs의 재귀호출 스택 깊이는 최악의 경우 N까지 커질 수 있습니다 -> O(N)
*/

func validTree(n int, edges [][]int) bool {
	// valid tree는 n-1개의 edge를 가질 수 밖에 없습validTree
	// 아래 판별식을 이용하면 유효하지 않은 input에 대해 상당한 연산을 줄일 수 있습니다
	if len(edges) != n-1 {
		return false
	}
	// 주어진 2차원 배열 edges를 이용해 adjacency list를 생성합니다
	adj := make([][]int, n)
	for _, edge := range edges {
		adj[edge[0]] = append(adj[edge[0]], edge[1])
		adj[edge[1]] = append(adj[edge[1]], edge[0])
	}
	// cycle이 있는지 여부를 판단하기 위해 visited라는 map을 생성합니다 (Go에서는 map으로 set 기능을 대신함)
	visited := make(map[int]bool)

	var dfs func(int, int) bool
	dfs = func(node int, parent int) bool {
		// cycle 발견시 false return
		if _, ok := visited[node]; ok {
			return false
		}
		visited[node] = true
		for _, next := range adj[node] {
			if next == parent {
				continue
			}
			if !dfs(next, node) {
				return false
			}
		}
		return true
	}
	// cycle 여부를 판단합니다
	if !dfs(0, -1) {
		return false
	}
	// node가 모두 연결되어 있는지 여부를 판단합니다
	return len(visited) == n
}
