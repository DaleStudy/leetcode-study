# Complexity
- Time Complexity: $O(M*N)$
  - 모든 섬을 방문하는 경우가 최대이며, 이 때 `grid`의 행의 길이인 M, 열의 길이인 N을 곱한 M*N만큼 재귀호출이 일어난다.
- Space Complexity: $O(M*N)$
  - 모든 섬의 방문 여부를 저장하기 위해 `grid`의 행의 길이인 M, 열의 길이인 N을 곱한 M*N 크기의 `visited` 배열을 선언했다.

# Code
```go
var offsets = [][]int{
	{1, 0},
	{-1, 0},
	{0, 1},
	{0, -1},
}

func update(i int, j int, grid [][]byte, visited [][]bool) {
	visited[i][j] = true
	for _, offset := range offsets {
		ni, nj := i+offset[0], j+offset[1]
		if ni < 0 || ni >= len(grid) || nj < 0 || nj >= len(grid[0]) || visited[ni][nj] || grid[ni][nj] == '0' {
			continue
		}
		update(ni, nj, grid, visited)
	}
}

func numIslands(grid [][]byte) int {
	visited := make([][]bool, len(grid))
	for i, _ := range visited {
		visited[i] = make([]bool, len(grid[0]))
	}

	var cnt int
	for i, row := range grid {
		for j, val := range row {
			if val == '0' || visited[i][j] {
				continue
			}
			update(i, j, grid, visited)
			cnt++
		}
	}
	return cnt
}

```