/**
 * 행렬에서 0을 찾아, 해당 요소의 전체 행과 열을 0으로 변환하는 문제
 *
 * 팔로우업: O(1) 공간 복잡도로 해결하기
 * - 원래 행렬의 첫번째 행과 열을 사용, 0이 있는 행과 열을 표시(추가 공간사용 없이)
 * 접근 방법:
 * 1. 첫번째 행과 열에 0이 있는지 확인, 있다면 별도의 변수에 저장
 * 2. 첫번째 행과 열을 제외한 나머지 행렬을 순회 ➡️ 0을 발견하면 해당 위치의 행과 열을 0으로 설정
 * 3. 설정된 마커 기반으로 내부 행렬의 요소를 0으로 업데이트
 *
 * 시간복잡도: O(m*n) ➡️ 행렬을 두번 순회
 * 공간복잡도: O(1) ➡️ 추가 배열 사용 안함
 */
/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function (matrix) {
  if (!matrix || matrix.length === 0 || matrix[0].length === 0) return;

  const m = matrix.length;
  const n = matrix[0].length;

  // 한번의 반복문으로 첫번째 행과 열을 체크
  let firstRowHasZero = false;
  let firstColHasZero = false;

  // 첫번째 행 체크
  for (let j = 0; j < n; j++) {
    if (matrix[0][j] === 0) {
      firstRowHasZero = true;
      break;
    }
  }
  // 첫번째 열 체크
  for (let i = 0; i < m; i++) {
    if (matrix[i][0] === 0) {
      firstColHasZero = true;
      break;
    }
  }

  // 첫번째 행과 열을 제외한 나머지 행렬을 순회, 마커 설정
  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      if (matrix[i][j] === 0) {
        matrix[i][0] = 0; // 해당 행의 첫번째 열을 0으로 마킹
        matrix[0][j] = 0; // 해당 열의 첫번째 행을 0으로 마킹
      }
    }
  }
  // 마커를 기반으로 내부 행렬의 요소를 0으로 업데이트
  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      if (matrix[i][0] === 0 || matrix[0][j] === 0) {
        matrix[i][j] = 0;
      }
    }
  }
  // 첫번째 행과 열을 업데이트
  if (firstRowHasZero) {
    for (let j = 0; j < n; j++) {
      matrix[0][j] = 0;
    }
  }
  if (firstColHasZero) {
    for (let i = 0; i < m; i++) {
      matrix[i][0] = 0;
    }
  }
};
