/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function (matrix) {
  let top = 0; // 상단 행 인덱스
  let bottom = matrix.length - 1; // 하단 행 인덱스
  let left = 0; // 좌측 열 인덱스
  let right = matrix[0].length - 1; // 우측 열 인덱스

  const answer = [];

  // 상단, 우측, 하단, 좌측 경계를 차례로 순회하며 값을 수집
  // 각 반복마다 경계가 안쪽으로 줄어듦
  while (top <= bottom && left <= right) {
    // 1. 상단 행 순회
    for (let col = left; col <= right; col++) {
      answer.push(matrix[top][col]);
    }
    top++; // 상단 경계를 아래로 한칸 이동
    // 상단 경계가 하단 경계를 넘어가면 중단
    if (top > bottom) {
      break;
    }
    // 2. 우측 열 순회
    for (let row = top; row <= bottom; row++) {
      answer.push(matrix[row][right]);
    }
    right--; // 우측 경계를 왼쪽으로 한칸 이동
    // 우측 경계가 좌측 경계를 넘어가면 중단
    if (left > right) {
      break;
    }
    // 3. 하단 행 순회
    for (let col = right; col >= left; col--) {
      answer.push(matrix[bottom][col]);
    }
    bottom--; // 하단 경계를 위쪽으로 한칸 이동

    // 4. 좌측 열 순회
    for (let row = bottom; row >= top; row--) {
      answer.push(matrix[row][left]);
    }
    left++; // 좌측 경계를 우측으로 한칸 이동
  }

  return answer;
};
