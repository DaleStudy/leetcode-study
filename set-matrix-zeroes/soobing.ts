/**
 * 문제 설명
 * - 0으로 표시된 좌표의 행과 열을 모두 0으로 만드는 문제
 * - 다른 메모리를 만들지 말고, 핵심은 in place!! 입력데이터를 수정해서 푸는것을 원함
 * - "in-place"로 풀라고 하면 보통은 O(1) 공간복잡도를 기대
 *
 * 아이디어
 * 1) 행렬을 전체 순회하면서 0의 위치를 set에 기억해놨다가 다시 순회하면서 변경 -> 공간 복잡도 O(m + n)
 *
 * 2) 첫번째 행과 열을 메모리로 사용 -> 공간 복잡도 O(1)
 * - 첫번째 행과 열에 0이 존재하는지 확인 후 변수로 따로 뺀다
 * - 나머지 셀 중에서 0이 존재하는지 순회하고 있으면 첫번째 행/열에 표시한다
 * - 나머지 셀을 다시 순회하면서 첫번째 열을 참고하여 0으로 치환한다
 * - 첫번째 행과 열을 0으로 바꿔아한다면 처리한다.
 */

/**
 1번 방법
 *
function setZeroes(matrix: number[][]): void {
  const rows = matrix.length;
  const cols = matrix[0].length;
  const zeroRows = new Set<number>();
  const zeroCols = new Set<number>();

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (matrix[r][c] === 0) {
        zeroRows.add(r);
        zeroCols.add(c);
      }
    }
  }

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (zeroRows.has(r) || zeroCols.has(c)) {
        matrix[r][c] = 0;
      }
    }
  }
}
*/

function setZeroes(matrix: number[][]): void {
  const rows = matrix.length;
  const cols = matrix[0].length;
  let firstRowHasZero = false;
  let firstColHasZero = false;

  // 첫번째 행과 열에 0이 존재하는지 확인
  for (let r = 0; r < rows; r++) {
    if (matrix[r][0] === 0) {
      firstColHasZero = true;
      break;
    }
  }
  for (let c = 0; c < cols; c++) {
    if (matrix[0][c] === 0) {
      firstRowHasZero = true;
      break;
    }
  }

  // 나머지 셀중에 0이 존재하는지 확인 후 첫번쨰 행과 열에 표시
  for (let r = 1; r < rows; r++) {
    for (let c = 1; c < cols; c++) {
      if (matrix[r][c] === 0) {
        matrix[r][0] = 0;
        matrix[0][c] = 0;
      }
    }
  }

  // 나머지 셀을 다시 순회하면서 첫번째 행/열이 0인 경우 같은 행/열도 0으로 변경
  for (let r = 1; r < rows; r++) {
    for (let c = 1; c < cols; c++) {
      if (matrix[r][0] === 0 || matrix[0][c] === 0) {
        matrix[r][c] = 0;
      }
    }
  }

  // 첫번째 행/열이 0인경우 해당 행/열도 0으로 변경
  if (firstRowHasZero) {
    for (let c = 0; c < cols; c++) {
      matrix[0][c] = 0;
    }
  }
  if (firstColHasZero) {
    for (let r = 0; r < rows; r++) {
      matrix[r][0] = 0;
    }
  }
}
