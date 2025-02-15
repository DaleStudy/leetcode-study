// w: width of grid, h: height of grid
// Time complexity: O(h*w)
// Space complexity: O(h*w)

class MyQueue {
  constructor() {
    this.q = [];
    this.front = 0;
    this.rear = 0;
  }

  get isEmpty() {
    return this.front === this.rear;
  }

  push(value) {
    this.q.push(value);
    this.rear++;
  }

  pop() {
    const value = this.q[this.front];
    delete this.q[this.front++];
    return value;
  }
}

/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {
  const h = grid.length;
  const w = grid[0].length;

  const dy = [1, 0, -1, 0];
  const dx = [0, 1, 0, -1];

  const bfs = (start) => {
    const q = new MyQueue();
    q.push(start);
    const [sy, sx] = start;
    grid[sy][sx] = "0";

    while (!q.isEmpty) {
      const [cy, cx] = q.pop();

      for (let i = 0; i < dy.length; i++) {
        const ny = cy + dy[i];
        const nx = cx + dx[i];

        if (ny >= 0 && ny < h && nx >= 0 && nx < w && grid[ny][nx] === "1") {
          q.push([ny, nx]);
          grid[ny][nx] = "0";
        }
      }
    }
  };

  let answer = 0;
  for (let i = 0; i < h; i++) {
    for (let j = 0; j < w; j++) {
      if (grid[i][j] === "1") {
        answer++;
        bfs([i, j]);
      }
    }
  }

  return answer;
};
