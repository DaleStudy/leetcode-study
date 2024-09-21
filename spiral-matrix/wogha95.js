/**
 * 2차 풀이: 기존 matrix 변경 없도록 개선
 *
 * TC: O(ROW * COLUMN)
 * matrix 전체 순회 1회
 *
 * SC: O(ROW * COLUMN)
 * 정답 제출을 위한 result 공간복잡도
 */

/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function (matrix) {
  const ROW = matrix.length;
  const COLUMN = matrix[0].length;
  // 1. 상하좌우 시작끝 index를 저장함
  const boundary = {
    top: 0,
    bottom: ROW - 1,
    left: 0,
    right: COLUMN - 1,
  };
  const result = [];

  while (result.length < ROW * COLUMN) {
    // 2. 오른쪽으로 순회
    for (let column = boundary.left; column <= boundary.right; column++) {
      result.push(matrix[boundary.top][column]);
    }
    boundary.top += 1;

    // 3. 아래로 순회
    for (let row = boundary.top; row <= boundary.bottom; row++) {
      result.push(matrix[row][boundary.right]);
    }
    boundary.right -= 1;

    // 4. 모두 순회했는데 왔던길 되돌아가는 경우를 막기위해 중간 조건문 추가
    if (result.length === ROW * COLUMN) {
      break;
    }

    // 5. 왼쪽으로 순회
    for (let column = boundary.right; column >= boundary.left; column--) {
      result.push(matrix[boundary.bottom][column]);
    }
    boundary.bottom -= 1;

    // 6. 위쪽으로 순회
    for (let row = boundary.bottom; row >= boundary.top; row--) {
      result.push(matrix[row][boundary.left]);
    }
    boundary.left += 1;
  }

  return result;
};

/**
 * 1차 풀이
 *
 * TC: O(ROW * COLUMN)
 * matrix 전체 순회 1회
 *
 * SC: O(ROW * COLUMN)
 * 정답 제출을 위한 result 공간복잡도
 */

/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function (matrix) {
  const ROW = matrix.length;
  const COLUMN = matrix[0].length;
  // 우하좌상 순서
  const DIRECTION = [
    {
      row: 0,
      column: 1,
    },
    {
      row: 1,
      column: 0,
    },
    {
      row: 0,
      column: -1,
    },
    {
      row: -1,
      column: 0,
    },
  ];

  // 1. 첫 시작점 방문표시
  const result = [matrix[0][0]];
  matrix[0][0] = "#";

  let current = {
    row: 0,
    column: 0,
  };
  let directionIndex = 0;

  // 2. 총 갯수만큼 채워질때까지 순회
  while (result.length < ROW * COLUMN) {
    const next = {
      row: current.row + DIRECTION[directionIndex].row,
      column: current.column + DIRECTION[directionIndex].column,
    };
    // 3. 다음 순회할 곳이 유효한 좌표인지 방문한 곳인지 확인
    if (
      !isValidPosition(next.row, next.column) ||
      matrix[next.row][next.column] === "#"
    ) {
      // 4. 방향 전환
      directionIndex = (directionIndex + 1) % 4;
    } else {
      // 5. 방문 표시 후 다음 좌표로 이동
      result.push(matrix[next.row][next.column]);
      matrix[next.row][next.column] = "#";
      current = next;
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
};
