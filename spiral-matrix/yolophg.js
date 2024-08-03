// Time Complexity: O(m*n) m = number of rows, n = number of cols
// Space Complexity: O(m*n)

var spiralOrder = function (matrix) {
  let result = [];

  while (matrix.length > 0) {
    // add the first row to the result
    result = result.concat(matrix.shift());

    // add the last element of each remaining row to the result
    for (let i = 0; i < matrix.length; i++) {
      if (matrix[i].length > 0) {
        result.push(matrix[i].pop());
      }
    }

    // add the last row in reverse order to the result, if any rows are left
    if (matrix.length > 0) {
      result = result.concat(matrix.pop().reverse());
    }

    // add the first element of each remaining row to the result in reverse order
    for (let i = matrix.length - 1; i >= 0; i--) {
      if (matrix[i].length > 0) {
        result.push(matrix[i].shift());
      }
    }
  }

  // return the result array containing the elements in spiral order
  return result;
};
