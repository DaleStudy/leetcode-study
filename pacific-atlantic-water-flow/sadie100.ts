/**
pacific에 닿을 수 있는 grid를 판별하는 이중 배열과 atlantic에 닿을 수 있는지를 판별하는 이중 배열을 생성한다.
pacific 배열은 r, c 중 하나라도 0일 경우 true값,
atlantic 배열은 r, c 중 하나라도 length값과 같을 경우 true값을 채운다

이후 r, c 탐색을 돌며 pacific/ atlantic true인 값이 있으면 dfs를 돌린다
 - 이전 heights값보다 크거나 같으면 true 처리, 인접한 셀을 또 dfs 탐색

두 배열값이 둘 다 true인 위치들을 리턴한다

시간복잡도 : O(M*N) - 순회
 */

function pacificAtlantic(heights: number[][]): number[][] {
  const m = heights.length
  const n = heights[0].length
  const result = []
  const pacificChecker = Array.from({ length: m }).map((el, idx) => {
    if (idx === 0) {
      return new Array(n).fill(true)
    } else {
      const arr = new Array(n).fill(false)
      arr[0] = true
      return arr
    }
  })
  const atlanticChecker = Array.from({ length: m }).map((el, idx) => {
    if (idx === m - 1) {
      return new Array(n).fill(true)
    } else {
      const arr = new Array(n).fill(false)
      arr[n - 1] = true
      return arr
    }
  })

  const dx = [0, 1, -1, 0]
  const dy = [1, 0, 0, -1]

  const search = (row, col, checker, stdValue) => {
    const value = heights[row][col]
    if (value < stdValue) return

    checker[row][col] = true

    for (let i = 0; i < 4; i++) {
      const newRow = row + dx[i]
      const newCol = col + dy[i]
      if (newRow < 0 || newRow >= m) continue
      if (newCol < 0 || newCol >= n) continue
      if (checker[newRow][newCol]) continue

      search(newRow, newCol, checker, value)
    }
  }

  // dfs 탐색
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (pacificChecker[i][j]) {
        search(i, j, pacificChecker, heights[i][j])
      }
      if (atlanticChecker[i][j]) {
        search(i, j, atlanticChecker, heights[i][j])
      }
    }
  }

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (pacificChecker[i][j] && atlanticChecker[i][j]) {
        result.push([i, j])
      }
    }
  }

  //pacific, atlantic 모두 true인 인덱스배열 반환
  return result
}
