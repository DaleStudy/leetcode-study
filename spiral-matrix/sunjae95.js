/**
 * @description
 * brainstorming:
 * just implement question
 *
 * m: length of matrix
 * n: length of matrix[i]
 * time complexity: O(m * n)
 * space complexity: O(m * n)
 */
var spiralOrder = function (matrix) {
  let count = matrix.length * matrix[0].length;
  let [r, c] = [1, 1];
  const answer = [];
  const MAX_R = matrix.length + 2;
  const MAX_C = matrix[0].length + 2;
  const visited = Array.from({ length: MAX_R }, (_, i) => {
    return Array.from(
      { length: MAX_C },
      (_, j) => i === 0 || i === MAX_R - 1 || j === 0 || j === MAX_C - 1
    );
  });

  while (count--) {
    const check = {
      left: c >= 1 && visited[r][c - 1],
      right: c < MAX_C - 1 && visited[r][c + 1],
      top: r >= 1 && visited[r - 1][c],
      bottom: r < MAX_R - 1 && visited[r + 1][c],
    };
    visited[r][c] = true;
    answer.push(matrix[r - 1][c - 1]);

    if (check.left && check.top && check.bottom) c++;
    else if (check.left && check.top && check.right) r++;
    else if (check.right && check.top && check.bottom) c--;
    else if (check.left && check.right && check.bottom) r--;
    else if (check.left && check.top) c++;
    else if (check.top && check.right) r++;
    else if (check.right && check.bottom) c--;
    else if (check.bottom && check.left) r--;
  }

  return answer;
};
