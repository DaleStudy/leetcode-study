/*
m x n visited 이중배열을 만들고 grid를 탐색,
visited false면서 1값이 있는 타일이 있으면 dfs로 상하좌우를 탐색, visited true로 만든 뒤 result+=1한다
탐색이 마치면 result를 리턴한다

시간복잡도 : O(M + N)
공간복잡도 : O(M + N) - visited
*/

const dx = [0, 1, -1, 0]
const dy = [1, 0, 0, -1]

function numIslands(grid: string[][]): number {
  const visited = Array.from({ length: grid.length }, () =>
    new Array(grid[0].length).fill(false),
  )
  let result = 0

  function search(row: number, col: number) {
    visited[row][col] = true

    for (let i = 0; i < 4; i++) {
      const newRow = row + dx[i]
      const newCol = col + dy[i]

      if (newRow < 0 || newRow >= grid.length) continue
      if (newCol < 0 || newCol >= grid[0].length) continue

      if (visited[newRow][newCol] === false && grid[newRow][newCol] === '1') {
        search(newRow, newCol)
      }
    }
  }

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (visited[i][j] === false && grid[i][j] === '1') {
        search(i, j)
        result += 1
      }
    }
  }

  return result
}
