// Time Complexity: O(n^2)
// Space Complexity: O(1)

var rotate = function (matrix) {
  const n = matrix.length;

  // perform the rotation layer by layer
  for (let layer = 0; layer < Math.floor(n / 2); layer++) {
    let first = layer;
    let last = n - 1 - layer;

    for (let i = first; i < last; i++) {
      let offset = i - first;

      // save the top element
      let top = matrix[first][i];

      // move left element to top
      matrix[first][i] = matrix[last - offset][first];

      // move bottom element to left
      matrix[last - offset][first] = matrix[last][last - offset];

      // move right element to bottom
      matrix[last][last - offset] = matrix[i][last];

      // assign saved top element to right
      matrix[i][last] = top;
    }
  }
};
