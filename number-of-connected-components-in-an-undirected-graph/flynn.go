/*
풀이
- DFS와 hashmap(set)을 이용하여 풀이할 수 있습니다
- 이전에 풀이했던 course schedule 문제와 유사합니다
Big O
- N: 노드 개수
- E: 간선의 개수
- Time complexity: O(N + E)
  - adj를 생성하는 반복문의 시간복잡도는 E에 비례하여 증가합니다
  - 전체 노드를 최대 1번씩 조회하므로 두번째 반복문의 시간복잡도는 N에 비례하여 증가합니다
- Space complexity: O(N + E)
  - adjacency list의 크기는 E에 비례하여 증가합니다
  - checked의 크기는 N에 비례하여 증가합니다
  - check 함수의 재귀 호출 스택 깊이 또한 최악의 경우, N에 비례하여 증가합니다
*/

func countComponents(n int, edges [][]int) int {
	adj := make(map[int][]int)
	for _, edge := range edges {
		adj[edge[0]] = append(adj[edge[0]], edge[1])
		adj[edge[1]] = append(adj[edge[1]], edge[0])
	}
	// Go는 {int: bool} hashmap을 set처럼 사용함
	checked := make(map[int]bool) // 모든 탐색이 끝난 노드를 기록함
	// 각 node를 조회하는 함수
	var check func(int)
	check = func(i int) {
		checked[i] = true
		for _, nxt := range adj[i] {
			if _, ok := checked[nxt]; ok {
				continue
			}
			check(nxt)
		}
	}

	res := 0
	for i := 0; i < n; i++ {
		if _, ok := checked[i]; ok {
			continue
		}
		res++
		check(i)
	}

	return res
}
