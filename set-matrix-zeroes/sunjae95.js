/**
 * @description
 * brainstorming:
 * memoization
 *
 * m: length of matrix
 * n: length of matrix[i]
 * time complexity: O(m * n)
 * space complexity: O(m * n)
 */
var setZeroes = function (matrix) {
  const stack = [];
  const memo = { row: new Set(), column: new Set() };

  const setZero = ({ r, c, isRow, isColumn }) => {
    const length = isRow ? matrix.length : matrix[0].length;

    for (let i = 0; i < length; i++) {
      const row = isRow ? i : r;
      const column = isColumn ? i : c;
      matrix[row][column] = 0;
    }
  };

  matrix.forEach((row, r) => {
    row.forEach((value, c) => {
      if (value === 0) stack.push([r, c]);
    });
  });

  while (stack.length) {
    const [r, c] = stack.pop();

    if (!memo.row.has(r)) {
      setZero({ r, c, isColumn: true });
      memo.row.add(r);
    }

    if (!memo.column.has(c)) {
      setZero({ r, c, isRow: true });
      memo.column.add(c);
    }
  }

  return matrix;
};
