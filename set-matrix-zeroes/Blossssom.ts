/**
 * @param matrix - 2중 배열 그리드
 * @description
 * - 요소가 0일 경우 속한 행과 열 전체를 0으로 변경
 *
 * - 풀이 1. 단순하게 0 목록을 만들어 해당 요소의 행과 열을 변경
 * - 풀이 2. 풀이 1은 매번 덮어씌우기를 진행하므로 행과 열 마다 첫번 째 요소를 메모장으로 사용.
 * - 내부를 탐색하며 진행
 */

// function setZeroes(matrix: number[][]): void {
//   const zeroes = [];

//   for (let i = 0; i < matrix.length; i++) {
//     for (let j = 0; j < matrix[0].length; j++) {
//       if (matrix[i][j] === 0) {
//         zeroes.push([i, j]);
//       }
//     }
//   }

//   for (let i = 0; i < zeroes.length; i++) {
//     const [row, col] = zeroes[i];
//     console.log(row, col);

//     matrix[row] = Array.from({ length: matrix[row].length }, () => 0);
//     console.log(matrix);

//     for (let j = 0; j < matrix.length; j++) {
//       matrix[j][col] = 0;
//     }
//   }
// }

function setZeroes(matrix: number[][]): void {
  const m = matrix.length;
  const n = matrix[0].length;
  let isFirstRowZero = false;
  let isFirstColZero = false;

  for (let i = 0; i < m; i++) {
    if (!matrix[i][0]) {
      isFirstColZero = true;
    }
  }

  for (let j = 0; j < n; j++) {
    if (!matrix[0][j]) {
      isFirstRowZero = true;
    }
  }

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      if (!matrix[i][j]) {
        matrix[i][0] = 0;
        matrix[0][j] = 0;
      }
    }
  }

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      if (matrix[i][0] === 0 || matrix[0][j] === 0) {
        matrix[i][j] = 0;
      }
    }
  }

  if (isFirstColZero) {
    for (let i = 0; i < m; i++) matrix[i][0] = 0;
  }
  if (isFirstRowZero) {
    for (let j = 0; j < n; j++) matrix[0][j] = 0;
  }
}

const matrix = [
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1],
];

setZeroes(matrix);


