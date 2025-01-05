// 시간복잡도: O(n^2 * 4^m)
// 공간복잡도: O(n * m)
// (n: board의 행의 개수, m: word의 길이)

package main

import "testing"

func TestExist(t *testing.T) {
	board := [][]byte{
		{'A', 'B', 'C', 'E'},
		{'S', 'F', 'C', 'S'},
		{'A', 'D', 'E', 'E'},
	}

	if !exist(board, "ABCCED") {
		t.Error("Test case 0 failed")
	}

	if !exist(board, "SEE") {
		t.Error("Test case 1 failed")
	}

	if exist(board, "ABCB") {
		t.Error("Test case 2 failed")
	}
}

func backtrack(board [][]byte, histories [][]bool, n_row int, n_col int, word string, idx int) bool {
	if idx == len(word) {
		return true
	}

	if n_row < 0 || n_row >= len(board) {
		return false
	}

	if n_col < 0 || n_col >= len(board[0]) {
		return false
	}

	if board[n_row][n_col] != word[idx] || histories[n_row][n_col] {
		return false
	}

	steps := [][]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}

	histories[n_row][n_col] = true

	for _, step := range steps {
		if backtrack(board, histories, n_row+step[0], n_col+step[1], word, idx+1) {
			return true
		}
	}

	histories[n_row][n_col] = false
	return false
}

func exist(board [][]byte, word string) bool {
	n_rows := len(board)
	n_cols := len(board[0])
	
	histories := make([][]bool, n_rows)

	for n_row := 0; n_row < n_rows; n_row++ {
		for n_col := 0; n_col < n_cols; n_col++ {
			if board[n_row][n_col] == word[0] {
				for k := 0; k < n_rows; k++ {
					histories[k] = make([]bool, n_cols)
				}

				if backtrack(board, histories, n_row, n_col, word, 0) {
					return true
				}
			}
		}
	}

	return false
}
