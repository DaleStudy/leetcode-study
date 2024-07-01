# Complexity
- Time Complexity: $O(V+E)$
  - 정점 수와 간선 수인 V와 E에 대해, dfs인 `hasCycle`을 모두 호출하는 데 비용 V가 발생하고 반복문을 모두 순회하는 데 비용 E가 발생하여 총 비용 `V+E`가 발생한다. 
- Space Complexity: $O(V+E)$
  - 정점 수와 간선 수인 V와 E에 대해, 인접 리스트 `adj`을 선언하는 데 비용 `V+E`가 발생한다.

# Code
```go
func hasCycle(curr int, adj [][]int, visited []bool, finish []bool) bool {
	if visited[curr] {
		return !finish[curr]
	}
	visited[curr] = true

	for _, next := range adj[curr] {
		if hasCycle(next, adj, visited, finish) {
			return true
		}
	}
	finish[curr] = true

	return false
}

func canFinish(numCourses int, prerequisites [][]int) bool {
	adj := make([][]int, numCourses)
	for i, _ := range adj {
		adj[i] = make([]int, 0)
	}
	for _, prerequisite := range prerequisites {
		from, to := prerequisite[0], prerequisite[1]
		adj[from] = append(adj[from], to)
	}

	visited := make([]bool, numCourses)
	finish := make([]bool, numCourses)
	for from := range adj {
		if hasCycle(from, adj, visited, finish) {
			return false
		}
	}
	return true
}

```