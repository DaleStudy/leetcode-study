/**
 * 2차 배열의 1로된 섬 구하기
 * 달레 알고리즘 해석을 참고하여 작성했습니다.
 * DFS(깊이 우선 알고리즘)
 * 알고리즘 복잡도
 * - 시간 복잡도: O(m x n)
 * - 공간 복잡도: O(m x n)
 * @param grid
 */
function numIslands(grid: string[][]): number {
    const rows = grid.length
    const cols = grid[0].length
    let islands = 0

    // 인접한 땅의 1을 찾아야 함 - 상하좌우
    const dfs = (i: number, j: number): void => {
        if (i < 0 || i >= rows || j < 0 || j >= cols || grid[i][j] !== '1') {
            return
        }

        grid[i][j] = '0' // 한번 확인한 경우 물로 바꿔줌

        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (grid[i][j] === '1') {
                dfs(i, j)
                islands++
            }
        }
    }

    return islands
}
