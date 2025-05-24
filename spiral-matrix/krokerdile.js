// Time: O(m * n)
// Space: O(1) + output array
function spiralOrder(matrix) {
    const result = [];
  
    let top = 0;
    let bottom = matrix.length - 1;
    let left = 0;
    let right = matrix[0].length - 1;
  
    while (top <= bottom && left <= right) {
      // 1. 왼 → 오
      for (let i = left; i <= right; i++) {
        result.push(matrix[top][i]);
      }
      top++;
  
      // 2. 위 → 아래
      for (let i = top; i <= bottom; i++) {
        result.push(matrix[i][right]);
      }
      right--;
  
      // 3. 오 → 왼
      if (top <= bottom) {
        for (let i = right; i >= left; i--) {
          result.push(matrix[bottom][i]);
        }
        bottom--;
      }
  
      // 4. 아래 → 위
      if (left <= right) {
        for (let i = bottom; i >= top; i--) {
          result.push(matrix[i][left]);
        }
        left++;
      }
    }
  
    return result;
}
