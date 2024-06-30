# Complexity
- Time complexity: $O(R*C)$
  - `board`의 행과 열이 크기인 R과 C에 대하여, 이들을 모두 순회할 수 있으므로 R*C가 소모된다.

- Space complexity: $O(R*C)$
  - `board`의 행과 열이 크기인 R과 C에 대하여, 방문 여부를 기록하는 2차원 배열(`visited`)과 콜스택의 최대 크기 모두 R*C이다.
# Code
```go
var offsets = [][]int{
	{1, 0},
	{-1, 0},
	{0, 1},
	{0, -1},
}

func makeVisited(rows, cols int) [][]bool {
	visited := make([][]bool, rows)
	for i := range visited {
		visited[i] = make([]bool, cols)
	}
	return visited
}

func existFrom(board [][]byte, i int, j int, word string, visited [][]bool) bool {
	if len(word) == 0 {
		return true
	} else if i < 0 || i >= len(board) || j < 0 || j >= len(board[0]) || board[i][j] != word[0] || visited[i][j] {
		return false
	}
	visited[i][j] = true
	defer func() { visited[i][j] = false }()

	for _, offset := range offsets {
		if existFrom(board, i+offset[0], j+offset[1], word[1:], visited) {
			return true
		}
	}
	return false
}

func exist(board [][]byte, word string) bool {
	for i, row := range board {
		for j, ch := range row {
			if ch == word[0] && existFrom(board, i, j, word, makeVisited(len(board), len(board[0]))) {
				return true
			}
		}
	}
	return false
}

```