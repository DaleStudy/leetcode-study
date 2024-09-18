/**
 * @description
 * brainstorming:
 * hash table + two pointer
 *
 * n = length of grid
 * k = length of grid[index]
 * time complexity: O(n * k)
 * space complexity: O(n * k)
 */
var numIslands = function (grid) {
  let answer = 0;
  const visited = Array.from({ length: grid.length }, (_, i) =>
    Array.from({ length: grid[i].length }, () => false)
  );

  const dfs = (r, c) => {
    const dr = [0, 1, 0, -1];
    const dc = [1, 0, -1, 0];

    for (let i = 0; i < 4; i++) {
      const nextR = r + dr[i];
      const nextC = c + dc[i];

      if (
        nextR >= 0 &&
        nextR < grid.length &&
        nextC >= 0 &&
        nextC < grid[r].length &&
        grid[nextR][nextC] == 1 &&
        !visited[nextR][nextC]
      ) {
        visited[nextR][nextC] = true;
        dfs(nextR, nextC);
      }
    }
  };

  for (let row = 0; row < grid.length; row++) {
    for (let column = 0; column < grid[row].length; column++) {
      if (grid[row][column] == 1 && !visited[row][column]) {
        visited[row][column] = true;
        answer++;
        dfs(row, column);
      }
    }
  }
  return answer;
};
