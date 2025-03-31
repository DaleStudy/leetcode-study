/**
 * 주어진 정사각형 행렬을 90도 회전시키는 함수
 *
 * @param {number[][]} matrix - 2차원 배열로 표현된 정사각형 행렬.
 *
 * 시간 복잡도: O(n^2)
 * - n * n 행렬, 모든 요소를 한 번씩 방문.
 *
 * 공간 복잡도: O(1)
 * - 추가적인 공간 사용 X
 */
function rotate(matrix: number[][]): void {
  // 행렬의 크기 n (정사각형 행렬이므로 행과 열의 수는 동일)
  const n = matrix.length;

  // 행렬의 대각선을 기준으로 좌표 (i, j)와 (j, i)의 요소를 교환.
  for (let i = 0; i < n; i++) {
      // j는 i부터 시작하여 중복 교환을 방지
      for (let j = i; j < n; j++) {
          // 배열 구조 분해 할당을 이용하여 두 요소를 스왑
          [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
      }
      // 각 행을 반전
      matrix[i].reverse();
  }
}

