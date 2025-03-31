/**
 Do not return anything, modify matrix in-place instead.
 */

/**
 *
 * 접근 방법 :
 *  - 1. matrix 순회하면서 대각선 기준으로 위쪽만 행과 열 값 바꾼다.
 *  - 2. 행 기준으로 reverse한다.
 *
 * 시간복잡도 : O(n^2)
 *  - n = matrix 행, 열 크기
 *  - matrix 순회 O(n^2)
 *
 * 공간복잡도 : O(1)
 *  - 추가 배열 사용하지 않음
 *
 */
function rotate(matrix: number[][]): void {
  for (let i = 0; i < matrix.length; i++) {
    for (let j = i + 1; j < matrix.length; j++) {
      [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
    }
  }

  for (let i = 0; i < matrix.length; i++) {
    matrix[i].reverse();
  }
}
