/**
 * 2차원 배열을 돌며 상하좌우로 이동할 수 연속하여 이동할 수 있는 공간(섬) 찾기
 * @param {sting[][]} grid - 2차원 배열
 * @returns {number} 만들 수 있는 공간(섬)의 갯수
 * 
 * 시간 복잡도: O(n * m)
 * m == grid.length
 * n == grid[i].length 
 * 
 * 공간 복잡도: O(n * m)
 * m == grid.length
 * n == grid[i].length 
 */
function numIslands(grid: string[][]): number {
    // 방문 배열 생성
    const visited: boolean[][] = Array.from(
      { length: grid.length },
      () => Array(grid[0].length).fill(false)
    );
  
    let islands = 0;
  
    const bfs = (i: number, j: number): void => {
      // 방문 처리
      visited[i][j] = true;
  
      // 상, 하, 좌, 우
      const directions: [number, number][] = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1],
      ];
  
      for (const direction of directions) {
        const nextI = i + direction[0];
        const nextJ = j + direction[1];
        if (
          nextI >= 0 &&
          nextI < grid.length &&
          nextJ >= 0 &&
          nextJ < grid[0].length &&
          !visited[nextI][nextJ] &&
          grid[nextI][nextJ] === '1'
        ) {
          bfs(nextI, nextJ);
        }
      }
    };
  
    for (let i = 0; i < grid.length; i++) {
      for (let j = 0; j < grid[0].length; j++) {
        if (grid[i][j] === '1' && !visited[i][j]) {
          // 새로운 섬 발견
          islands++;
  
          // BFS 실행
          bfs(i, j);
        }
      }
    }
  
    return islands;
}

