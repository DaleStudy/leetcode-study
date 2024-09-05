/*
 * TC: O(row * column * 4^words.length)
 * SC: O(n)
 * */
function exist(board: string[][], word: string): boolean {
  const words = word.split("");
  const n = words.length;

  const rowLen = board.length;
  const columnLen = board[0].length;

  const dfs = (row: number, column: number, cursor: number) => {
    if (cursor === n) {
      return true;
    }

    if (
      row < 0 ||
      row >= rowLen ||
      column < 0 ||
      column >= columnLen ||
      board[row][column] !== words[cursor]
    ) {
      return false;
    }

    const current = board[row][column];
    board[row][column] = "";

    if (
      dfs(row - 1, column, cursor + 1) ||
      dfs(row + 1, column, cursor + 1) ||
      dfs(row, column - 1, cursor + 1) ||
      dfs(row, column + 1, cursor + 1)
    ) {
      return true;
    }

    board[row][column] = current;

    return false;
  };

  for (let row = 0; row < rowLen; row++) {
    for (let column = 0; column < columnLen; column++) {
      if (dfs(row, column, 0)) {
        return true;
      }
    }
  }

  return false;
}

const t1 = exist(
  [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"],
  ],
  "ABCCED",
);
console.info("🚀 : tolluset.ts:5: t1=", t1); // true

const t2 = exist(
  [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"],
  ],
  "SEE",
);
console.info("🚀 : tolluset.ts:15: t2=", t2); // true

const t3 = exist(
  [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"],
  ],
  "ABCB",
);
console.info("🚀 : tolluset.ts:24: t3=", t3); // false
