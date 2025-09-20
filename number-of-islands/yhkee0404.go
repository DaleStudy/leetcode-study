var DRCS = [][]int{
    {0, -1,},
    {0, 1,},
    {-1, 0,},
    {1, 0,},
}

func numIslands(grid [][]byte) int {
    visited := make([][]bool, len(grid)) // S(n) = O(n)
    for i, row := range grid {
        visited[i] = make([]bool, len(row))
    }
    ans := 0
    stack := [][]int{}
    for i, row := range grid {
        for j, c := range row {
            if visited[i][j] || c == '0' {
                continue
            }
            ans++
            visited[i][j] = true
            stack = append(stack, []int{i, j})
            for len(stack) != 0 { // T(n) = O(n)
                u := stack[len(stack) - 1]
                stack = stack[: len(stack) - 1]
                for _, drc := range DRCS {
                    x := u[0] + drc[0]
                    y := u[1] + drc[1]
                    if x == -1 || x == len(grid) || y == -1 || y == len(row) ||
                            grid[x][y] == '0' || visited[x][y] {
                        continue
                    }
                    visited[x][y] = true
                    stack = append(stack, []int{x, y})
                }
            }
        }
    }
    return ans
}
