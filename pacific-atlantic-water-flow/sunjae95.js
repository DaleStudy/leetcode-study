/**
 * @description
 * brainstorming:
 * bfs + memoization
 *
 * n = length of height
 * m = length of height[i]
 * time complexity: O(n*m * 4^n*m)
 * space complexity: O(n*m)
 */
var pacificAtlantic = function (heights) {
  const visited = Array.from({ length: heights.length }, (_, i) =>
    Array.from({ length: heights[i].length }, () => false)
  );
  const memo = new Map();

  const bfs = (row, column) => {
    const dr = [0, 0, -1, 1];
    const dc = [1, -1, 0, 0];
    const queue = [[row, column]];
    let [pacific, atlantic] = [false, false];
    let queueIndex = 0;

    while (queueIndex !== queue.length) {
      const currentLastLength = queue.length;

      while (queueIndex !== currentLastLength) {
        const [r, c] = queue[queueIndex++];
        visited[r][c] = `${row},${column}`;

        if (memo.has(`${r},${c}`)) {
          memo.set(`${row},${column}`, [row, column]);
          return;
        }

        for (let i = 0; i < 4; i++) {
          const nextR = r + dr[i];
          const nextC = c + dc[i];
          const isPacific = nextR === -1 || nextC === -1;
          const isAtlantic =
            nextR === heights.length || nextC === heights[0].length;

          if (isPacific) {
            pacific = true;
            continue;
          }
          if (isAtlantic) {
            atlantic = true;
            continue;
          }

          if (visited[nextR][nextC] === `${row},${column}`) continue;

          if (heights[r][c] < heights[nextR][nextC]) continue;

          queue.push([nextR, nextC]);
        }
      }

      if (pacific && atlantic) {
        memo.set(`${row},${column}`, [row, column]);
        return;
      }
    }
  };

  for (let row = 0; row < heights.length; row++) {
    for (let column = 0; column < heights[row].length; column++) {
      bfs(row, column);
    }
  }

  return [...memo.values()];
};
