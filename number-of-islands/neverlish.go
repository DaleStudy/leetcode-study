// 시간복잡도: O(n^2)
// 공간복잡도: O(n)

package main

import "testing"

func TestNumIslands(t *testing.T) {
	result1 := numIslands([][]byte{
		{'1', '1', '1', '1', '0'},
		{'1', '1', '0', '1', '0'},
		{'1', '1', '0', '0', '0'},
		{'0', '0', '0', '0', '0'},
	})

	if result1 != 1 {
		t.Errorf("Expected 1, but got %v", result1)
	}

	result2 := numIslands([][]byte{
		{'1', '1', '0', '0', '0'},
		{'1', '1', '0', '0', '0'},
		{'0', '0', '1', '0', '0'},
		{'0', '0', '0', '1', '1'},
	})

	if result2 != 3 {
		t.Errorf("Expected 3, but got %v", result2)
	}
}

func dfs(grid [][]byte, i, j int) {
	if i < 0 || j < 0 || i >= len(grid) || j >= len(grid[i]) || grid[i][j] == '0' {
		return
	}

	grid[i][j] = '0'

	dfs(grid, i-1, j)
	dfs(grid, i+1, j)
	dfs(grid, i, j-1)
	dfs(grid, i, j+1)
}

func numIslands(grid [][]byte) int {
	result := 0

	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			if grid[i][j] == '1' {
				result++
				dfs(grid, i, j)
			}
		}
	}

	return result
}
