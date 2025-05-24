// TC: O(m * n)
// SC: O(1), if excluding the out array

function spiralOrder(matrix: number[][]): number[] {
  let n_rows = matrix.length;
  let n_cols = matrix[0].length;
  let row = 0;
  let col = -1;
  let direction = 1;

  const output: number[] = [];

  while (n_rows > 0 && n_cols > 0) {
    // move horizontally: right or left
    for (let i = 0; i < n_cols; i++) {
      col += direction; // in first iteration, direction = 1
      output.push(matrix[row][col]);
    }
    n_rows -= 1;

    // move vertically: down or up
    for (let j = 0; j < n_rows; j++) {
      row += direction;
      output.push(matrix[row][col]);
    }
    n_cols -= 1;

    // change direction
    direction *= -1;
  }

  return output;
}


// TC: O(m * n)
// SC: O(1), if excluding the out array

// function spiralOrder(matrix: number[][]): number[] {
//   // move: right -> down -> left -> up -> right -> ...
//   // matrix = [[1,2,3],[4,5,6],[7,8,9]]

//   let top = 0;
//   let bottom = matrix.length - 1;
//   let left = 0;
//   let right = matrix[0].length - 1;
//   let result: number[] = [];

//   while (top <= bottom && left <= right) {
//     // to the right
//     for (let col = left; col <= right; col++) {
//       result.push(matrix[top][col]);
//     }
//     top += 1;

//     // down
//     for (let row = top; row <= bottom; row++) {
//       result.push(matrix[row][right]);
//     }
//     right -= 1;

//     // to the left
//     // check needed because top was updated above
//     if (top <= bottom) {
//       for (let col = right; col >= left; col--) {
//         result.push(matrix[bottom][col]);
//       }
//       bottom -= 1;
//     }

//     // up
//     // check needed because right was updated above
//     if (left <= right) {
//       for (let row = bottom; row >= top; row--) {
//         result.push(matrix[row][left]);
//       }
//       left += 1;
//     }
//   }

//   return result;
// }

