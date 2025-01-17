/**
 * @link https://leetcode.com/problems/spiral-matrix/description/
 *
 * 접근 방법 :
 *  - right -> bottom -> left -> top 순서로 진행하면서 경계 업데이트 처리
 *
 * 시간복잡도 : O(n)
 *  - n은 행렬의 모든 숫자로, 모든 숫자를 한 번씩 방문하므로 O(n)
 *
 * 공간복잡도 : O(n)
 *  - 모든 숫자를 저장하기 위해서 배열 사용하므로 O(n)
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
