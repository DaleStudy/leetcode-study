// Time Complexity: O(m * n), where m is the number of rows and n is the number of columns in the matrix,
// because every element is processed once.

// Space Complexity: O(m * n), where m is the number of rows and n is the number of columns in the matrix,
// because we store all matrix elements in the result array.

/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function (matrix) {
    
  let topRow = 0;
  let bottomRow = matrix.length - 1;
  let leftCol = 0;
  let rightCol = matrix[0].length - 1;
  let result = [];

  while (topRow <= bottomRow && leftCol <= rightCol) {
    // move to the right
    for (let col = leftCol; col <= rightCol; col++) {
      result.push(matrix[topRow][col]);
    }

    topRow += 1;

    if (topRow > bottomRow) {
      break;
    }

    // move down
    for (let row = topRow; row <= bottomRow; row++) {
      result.push(matrix[row][rightCol]);
    }

    rightCol -= 1;

    if (leftCol > rightCol) {
      break;
    }

    // move to the left
    for (let col = rightCol; col >= leftCol; col--) {
      result.push(matrix[bottomRow][col]);
    }

    bottomRow -= 1;
    if (topRow > bottomRow) {
      break;
    }

    // move up
    for (let row = bottomRow; row >= topRow; row--) {
      result.push(matrix[row][leftCol]);
    }

    leftCol += 1;

    if (leftCol > rightCol) {
      break;
    }
  }

  return result;
};

