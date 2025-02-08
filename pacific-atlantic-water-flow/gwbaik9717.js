// n: height, m: width
// Time complexity: O(n*m)
// Space complexity: O(n*m)

class _Queue {
  constructor() {
    this.q = [];
    this.start = 0;
    this.end = 0;
  }

  isEmpty() {
    return this.start === this.end;
  }

  push(value) {
    this.q.push(value);
    this.end++;
  }

  pop() {
    const rv = this.q[this.start];
    delete this.q[this.start++];
    return rv;
  }
}
/**
 * @param {number[][]} heights
 * @return {number[][]}
 */
var pacificAtlantic = function (heights) {
  const dy = [1, 0, -1, 0];
  const dx = [0, 1, 0, -1];

  const h = heights.length;
  const w = heights[0].length;
  const checked = Array.from({ length: h }, () =>
    Array.from({ length: w }, () => [false, false])
  );

  // 태평양
  const pacific = new _Queue();

  for (let i = 0; i < h; i++) {
    if (!checked[i][0][0]) {
      pacific.push([i, 0]);
      checked[i][0][0] = true;
    }
  }

  for (let i = 0; i < w; i++) {
    if (!checked[0][i][0]) {
      pacific.push([0, i]);
      checked[0][i][0] = true;
    }
  }

  while (!pacific.isEmpty()) {
    const [cy, cx] = pacific.pop();

    for (let i = 0; i < dy.length; i++) {
      const ny = cy + dy[i];
      const nx = cx + dx[i];

      if (
        ny >= 0 &&
        ny < h &&
        nx >= 0 &&
        nx < w &&
        !checked[ny][nx][0] &&
        heights[ny][nx] >= heights[cy][cx]
      ) {
        checked[ny][nx][0] = true;
        pacific.push([ny, nx]);
      }
    }
  }

  // 대서양
  const answer = [];
  const atlantic = new _Queue();

  for (let i = 0; i < h; i++) {
    if (!checked[i][w - 1][1]) {
      atlantic.push([i, w - 1]);
      checked[i][w - 1][1] = true;
    }

    if (checked[i][w - 1][0] === true) {
      answer.push([i, w - 1]);
    }
  }

  for (let i = 0; i < w; i++) {
    if (!checked[h - 1][i][1]) {
      atlantic.push([h - 1, i]);
      checked[h - 1][i][1] = true;

      if (checked[h - 1][i][0] === true) {
        answer.push([h - 1, i]);
      }
    }
  }

  while (!atlantic.isEmpty()) {
    const [cy, cx] = atlantic.pop();

    for (let i = 0; i < dy.length; i++) {
      const ny = cy + dy[i];
      const nx = cx + dx[i];

      if (
        ny >= 0 &&
        ny < h &&
        nx >= 0 &&
        nx < w &&
        !checked[ny][nx][1] &&
        heights[ny][nx] >= heights[cy][cx]
      ) {
        if (checked[ny][nx][0] === true) {
          answer.push([ny, nx]);
        }

        checked[ny][nx][1] = true;
        atlantic.push([ny, nx]);
      }
    }
  }

  return answer;
};
