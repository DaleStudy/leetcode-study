function spiralOrder(matrix: number[][]): number[] {
  const rows = matrix.length;
  const cols = matrix[0].length;
  const total = rows * cols;
  let srow = 0; // start row
  let scol = 0;
  let erow = rows - 1; // end row
  let ecol = cols - 1;
  let count = 0;
  const ans: number[] = [];

  while (count < total) {
    for (let i = scol; i <= ecol && count < total; i++) {
      ans.push(matrix[srow][i]);
      count++;
    }
    srow++;
    for (let i = srow; i <= erow && count < total; i++) {
      ans.push(matrix[i][ecol]);
      count++;
    }
    ecol--;
    for (let i = ecol; i >= scol && count < total; i--) {
      ans.push(matrix[erow][i]);
      count++;
    }
    erow--;
    for (let i = erow; i >= srow && count < total; i--) {
      ans.push(matrix[i][scol]);
      count++;
    }
    scol++;
  }

  return ans;
}

// TC: O(m*n)
// SC: O(m*n)
