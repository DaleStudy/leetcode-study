/**
 * TC: O(ROW * COLUMN)
 * 주어진 grid 배열 전체 순회 + (최악의 경우 queue에서 grid 전체 순회)
 *
 * SC: O(ROW * COLUMN)
 * queue에서 최대 grid만큼 순회
 *
 * ROW: grid.length, COLUMN: grid[0].length
 */

/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {
  const LAND = "1";
  const VISITED_LAND = "#";
  const ROW = grid.length;
  const COLUMN = grid[0].length;

  // 1. 상하좌우 방향키
  const DIRECTION = [
    { r: 0, c: 1 },
    { r: 1, c: 0 },
    { r: 0, c: -1 },
    { r: -1, c: 0 },
  ];

  let numberOfIslands = 0;

  // 2. 전체 순회하면서
  for (let row = 0; row < ROW; row++) {
    for (let column = 0; column < COLUMN; column++) {
      // 3. LAND를 발견하면 방문한 섬으로 표시(bfs)하고 섬갯수 갱신
      if (grid[row][column] === LAND) {
        bfs(row, column);
        numberOfIslands += 1;
      }
    }
  }

  return numberOfIslands;

  function bfs(startRow, startColumn) {
    // 4. 시작좌표 queue에 넣고 방문 표시
    const queue = [[startRow, startColumn]];
    grid[startRow][startColumn] = VISITED_LAND;

    while (queue.length > 0) {
      const [row, column] = queue.shift();

      // 5. 상하좌우의 좌표를 가지고
      for (const direction of DIRECTION) {
        const nextRow = row + direction.r;
        const nextColumn = column + direction.c;

        // 6. 유효한 좌표 && 미방문 육지인지 확인
        if (
          isValidPosition(nextRow, nextColumn) &&
          grid[nextRow][nextColumn] === LAND
        ) {
          // 7. queue에 추가하고 방문 표시
          grid[nextRow][nextColumn] = VISITED_LAND;
          queue.push([nextRow, nextColumn]);
        }
      }
    }
  }

  // 8. 주어진 2차원 배열의 유효한 좌표인지 확인하는 함수
  function isValidPosition(row, column) {
    if (row < 0 || ROW <= row) {
      return false;
    }
    if (column < 0 || COLUMN <= column) {
      return false;
    }
    return true;
  }
};
