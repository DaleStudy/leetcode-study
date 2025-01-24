/**
 Do not return anything, modify matrix in-place instead.
 */
/**
 * @link https://leetcode.com/problems/set-matrix-zeroes/description/
 *
 * 접근 방법 :
 * - 행렬 순회하면서 0이 있는 행과 열을 rowsToZero과 colsToZero에 저장
 * - 다시 행렬 순회하면서 rowsToZero과 colsToZero와 포함된 경우 0으로 변경
 *
 * 시간복잡도 : O(m * n)
 *  - m * n 행렬 크기만큼 순회
 *
 * 공간복잡도 : O(m + n)
 *  - m 행과 n 열 정보 저장
 */
function setZeroes(matrix: number[][]): void {
  const rows = matrix.length;
  const cols = matrix[0].length;
  const rowsToZero = new Set<number>();
  const colsToZero = new Set<number>();
  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      if (matrix[row][col] === 0) {
        rowsToZero.add(row);
        colsToZero.add(col);
      }
    }
  }

  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      if (rowsToZero.has(row) || colsToZero.has(col)) {
        matrix[row][col] = 0;
      }
    }
  }
}

// 공간 복잡도 O(m+n)을 O(1)로 개선하기
// set에 행과 열 정보 저장하던 방식을 set없이 첫 번째 행과 열을 활용하는 방법으로 변경
function setZeroes(matrix: number[][]): void {
  const rows = matrix.length;
  const cols = matrix[0].length;
  let hasZeroInFirstRow = false;
  let hasZeroInFirstCol = false;

  // 첫 번째 열에 0 있는지 여부를 플래그로 저장
  for (let row = 0; row < rows; row++) {
    if (matrix[row][0] === 0) hasZeroInFirstCol = true;
  }

  // 첫 번째 행에 0 있는지 여부를 플래그로 저장
  for (let col = 0; col < cols; col++) {
    if (matrix[0][col] === 0) hasZeroInFirstRow = true;
  }

  // 첫 번째 행과 열 제외하고 마커 설정하기
  for (let row = 1; row < rows; row++) {
    for (let col = 1; col < cols; col++) {
      if (matrix[row][col] === 0) {
        matrix[0][col] = 0;
        matrix[row][0] = 0;
      }
    }
  }

  // 마커 기반으로 행렬에 반영
  for (let row = 1; row < rows; row++) {
    for (let col = 1; col < cols; col++) {
      if (matrix[row][0] === 0 || matrix[0][col] === 0) matrix[row][col] = 0;
    }
  }

  // 첫 번째 행 업데이트
  if (hasZeroInFirstRow) {
    for (let col = 0; col < cols; col++) {
      matrix[0][col] = 0;
    }
  }

  // 첫 번째 열 업데이트
  if (hasZeroInFirstCol) {
    for (let row = 0; row < rows; row++) {
      matrix[row][0] = 0;
    }
  }
}
