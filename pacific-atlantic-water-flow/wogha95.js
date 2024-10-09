/**
 * pacific(0행, 0열), atlantic(row-1행, column-1열)에서 높이가 같거나 높은 곳으로 순회한다.
 * 그리고 pacific에서 온 물과 atlantic에서 온 물이 만나는 곳을 정답으로 만든다.
 *
 * TC: O(row * column)
 * queue에 최대 row * column만큼 들어갑니다.
 *
 * SC: O(row * column)
 * pacific 또는 atlantic에 최대 row * column만큼 들어갑니다.
 */

/**
 * @param {number[][]} heights
 * @return {number[][]}
 */
var pacificAtlantic = function (heights) {
  const ROW = heights.length;
  const COLUMN = heights[0].length;
  const DIRECTION = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];
  const result = [];
  const queue = [];

  for (let c = 0; c < COLUMN; c++) {
    queue.push([0, c]);
  }
  for (let r = 1; r < ROW; r++) {
    queue.push([r, 0]);
  }

  const pacific = new Set();
  while (queue.length > 0) {
    const [row, column] = queue.shift();
    pacific.add(generateKey(row, column));
    for (const [directionR, directionC] of DIRECTION) {
      const [nextRow, nextColumn] = [row + directionR, column + directionC];
      if (
        isValidPosition(nextRow, nextColumn) &&
        heights[row][column] <= heights[nextRow][nextColumn] &&
        !pacific.has(generateKey(nextRow, nextColumn))
      ) {
        queue.push([nextRow, nextColumn]);
      }
    }
  }

  for (let c = 0; c < COLUMN; c++) {
    queue.push([ROW - 1, c]);
  }
  for (let r = 0; r < ROW - 1; r++) {
    queue.push([r, COLUMN - 1]);
  }

  const atlantic = new Set();
  while (queue.length > 0) {
    const [row, column] = queue.shift();
    const key = generateKey(row, column);
    atlantic.add(key);
    if (pacific.has(key)) {
      pacific.delete(key);
      result.push([row, column]);
    }
    for (const [directionR, directionC] of DIRECTION) {
      const [nextRow, nextColumn] = [row + directionR, column + directionC];
      if (
        isValidPosition(nextRow, nextColumn) &&
        heights[row][column] <= heights[nextRow][nextColumn] &&
        !atlantic.has(generateKey(nextRow, nextColumn))
      ) {
        queue.push([nextRow, nextColumn]);
      }
    }
  }

  return result;

  function isValidPosition(row, column) {
    if (row < 0 || ROW <= row) {
      return false;
    }
    if (column < 0 || COLUMN <= column) {
      return false;
    }
    return true;
  }

  function generateKey(row, column) {
    return `${row},${column}`;
  }
};
