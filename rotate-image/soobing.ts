/**
 * 문제 설명
 * - 2차원 배열을 90도 in-place로 회전하기
 *
 * 아이디어
 * 1) 대각선 이동 + 좌우 이동
 *
 */
/**
 Do not return anything, modify matrix in-place instead.
 */
function rotate(matrix: number[][]): void {
  const n = matrix.length;
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      const temp = matrix[i][j];
      matrix[i][j] = matrix[j][i];
      matrix[j][i] = temp;
    }
  }

  for (let i = 0; i < n; i++) {
    matrix[i].reverse();
  }
}
