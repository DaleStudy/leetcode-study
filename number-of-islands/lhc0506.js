/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
  const m = grid.length;
  const n = grid[0].length;
  const visited = Array.from(new Array(m), () => new Array(n).fill(false));
  const directions = [[0, 1], [0, -1], [1, 0], [-1, 0]];

  let islandCount = 0;

  for (let i = 0; i < m; i++) {
      for (let j = 0; j < n; j++) {
          if (grid[i][j] === '1' && !visited[i][j]) {
              const queue = [[i, j]];
              visited[i][j] = true;

              while (queue.length) {
                  const [y, x] = queue.shift();

                  for (const [dy, dx] of directions) {
                      const newY = y + dy;
                      const newX = x + dx;

                      if (newY >= 0 && newY < m && newX >= 0 && newX < n && grid[newY][newX] === '1' && !visited[newY][newX]) {
                          visited[newY][newX] = true;
                          queue.push([newY, newX]);
                      }
                  }
              }

              islandCount += 1;
          }
      }
  }

  return islandCount;
};

// 시간복잡도: O(m * n)
// 공간복잡도: O(m * n)
