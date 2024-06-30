# Complexity
- Time Complexity: $O(R*C)$
  - `heights`의 행과 열인 R과 C에 대해, 반복문과 DFS의 비용인 `R*C`가 발생한다. 
- Space Complexity: $O(R*C)$
  - `heights`의 행과 열인 R과 C에 대해, 방문 여부를 기록하는 배열(`pacifics`, `atlantics`)의 크기 비용인 `R*C`가 발생한다.

# Code
```go
var offsets = [][]int{
	{1, 0},
	{-1, 0},
	{0, 1},
	{0, -1},
}

func update(i int, j int, heights [][]int, visited [][]bool) {
	visited[i][j] = true

	for _, offset := range offsets {
		ni, nj := i+offset[0], j+offset[1]

		if ni < 0 || ni >= len(visited) || nj < 0 || nj >= len(visited[0]) || visited[ni][nj] || heights[i][j] > heights[ni][nj] {
			continue
		}
		update(ni, nj, heights, visited)
	}
}

func pacificAtlantic(heights [][]int) [][]int {
	parcifics := make([][]bool, len(heights))
	for i, _ := range parcifics {
		parcifics[i] = make([]bool, len(heights[0]))
	}
	atlantics := make([][]bool, len(heights))
	for i, _ := range atlantics {
		atlantics[i] = make([]bool, len(heights[0]))
	}

	for i, _ := range heights {
		for j, _ := range heights[0] {
			if i == 0 || j == 0 {
				update(i, j, heights, parcifics)
			}
			if i == len(heights)-1 || j == len(heights[0])-1 {
				update(i, j, heights, atlantics)
			}
		}
	}
	boths := make([][]int, 0)
	for i, _ := range heights {
		for j, _ := range heights[0] {
			if !(parcifics[i][j] && atlantics[i][j]) {
				continue
			}
			boths = append(boths, []int{i, j})
		}
	}
	return boths
}

```