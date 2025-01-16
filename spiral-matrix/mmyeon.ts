/**
 * @link https://leetcode.com/problems/spiral-matrix/description/
 *
 * 접근 방법 :
 *  - right -> bottom -> left -> top 순서로 진행하면서 경계 업데이트 처리
 *
 * 시간복잡도 : O(m x n)
 *  - m x n 행렬의 모든 숫자 방문하니까 O(m x n)
 *
 * 공간복잡도 : O(n)
 *  - 숫자 길이만큼 배열에 담음 *
 */

function spiralOrder(matrix: number[][]): number[] {
  const result: number[] = [];
  // 경계 설정
  let top = 0,
    bottom = matrix.length - 1,
    left = 0,
    right = matrix[0].length - 1;

  const moveRight = () => {
    for (let i = left; i <= right; i++) {
      result.push(matrix[top][i]);
    }
    top++;
  };

  const moveDown = () => {
    for (let i = top; i <= bottom; i++) {
      result.push(matrix[i][right]);
    }
    right--;
  };

  const moveLeft = () => {
    for (let i = right; i >= left; i--) {
      result.push(matrix[bottom][i]);
    }
    bottom--;
  };

  const moveUp = () => {
    for (let i = bottom; i >= top; i--) {
      result.push(matrix[i][left]);
    }
    left++;
  };

  while (top <= bottom && left <= right) {
    moveRight();
    moveDown();

    if (top <= bottom) moveLeft();
    if (left <= right) moveUp();
  }

  return result;
}
