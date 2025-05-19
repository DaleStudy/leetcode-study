/**
 * 오른쪽 -> 아래쪽 -> 왼쪽 -> 위쪽
 * --- 행렬의 경계 ---
 * top: 위쪽 경계
 * bottom: 아래쪽 경계
 * left: 왼쪽 경계
 * right: 오른쪽 경계
 * ----------------
 * 각 방향으로 한 바퀴를 돌 때마다 경계를 하나씩 줄여가며 모든 요소를 방문
 */

/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function (matrix) {
  if (!matrix.length || !matrix[0].length) return []; // 빈 행렬 체크

  const result = []; // 결과를 저장할 배열 초기화

  let top = 0;
  let bottom = matrix.length - 1;
  let left = 0;
  let right = matrix[0].length - 1;

  // 아직 처리할 요소가 남아있는 동안 계속 순회
  // top > bottom 또는 left > right가 되면 모든 요소를 방문한 것
  while (top <= bottom && left <= right) {
    // 1. 위쪽 행: 왼쪽 → 오른쪽 이동
    for (let i = left; i <= right; i++) {
      result.push(matrix[top][i]);
    }
    // 위쪽 행을 처리했으므로 top 인덱스를 1 증가
    top++;

    // 2. 오른쪽 열: 위 → 아래 이동
    for (let i = top; i <= bottom; i++) {
      result.push(matrix[i][right]);
    }
    // 오른쪽 열을 처리했으므로 right 인덱스를 1 감소
    right--;

    // 3. 아래쪽 행: 오른쪽 → 왼쪽 이동
    // 이미 top이 bottom을 초과한 경우, 아래쪽 행이 존재하지 않으므로 처리하지 않음
    if (top <= bottom) {
      // 현재 bottom 행에서 right부터 left까지의 모든 요소를 역순으로 순회
      for (let i = right; i >= left; i--) {
        result.push(matrix[bottom][i]);
      }
      // 아래쪽 행을 처리했으므로 bottom 인덱스를 1 감소
      bottom--;
    }

    // 4. 왼쪽 열: 아래 → 위 이동
    // 이미 left가 right를 초과한 경우, 왼쪽 열이 존재하지 않으므로 처리하지 않음
    if (left <= right) {
      // 현재 left 열에서 bottom부터 top까지의 모든 요소를 역순으로 순회
      for (let i = bottom; i >= top; i--) {
        result.push(matrix[i][left]);
      }
      // 왼쪽 열을 처리했으므로 left 인덱스를 1 증가
      left++;
    }
  }

  return result;
};
