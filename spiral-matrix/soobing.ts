/**
 *
 * 문제 설명
 * - 2차원 배열을 나선형으로 데이터 순회하여 1차원 배열로 담기
 * - 문제 풀이 타입의 알고리즘 문제 같음
 *
 * 아이디어
 * 1) 경계를 정하고 오른쪽, 아래, 왼쪽, 위로 순회한다.
 *
 */
function spiralOrder(matrix: number[][]): number[] {
  let left = 0;
  let top = 0;
  let right = matrix[0].length - 1;
  let bottom = matrix.length - 1;

  const result: number[] = [];

  while (left <= right && top <= bottom) {
    // 오른쪽
    for (let i = left; i <= right; i++) {
      result.push(matrix[top][i]);
    }
    top++;

    // 아래
    for (let i = top; i <= bottom; i++) {
      result.push(matrix[i][right]);
    }
    right--;

    // 왼쪽
    if (top <= bottom) {
      for (let i = right; i >= left; i--) {
        result.push(matrix[bottom][i]);
      }
      bottom--;
    }

    // 위쪽
    if (left <= right) {
      for (let i = bottom; i >= top; i--) {
        result.push(matrix[i][left]);
      }
      left++;
    }
  }
  return result;
}
