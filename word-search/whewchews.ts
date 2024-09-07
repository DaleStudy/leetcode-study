/*
* 조건
* 같은 단어 위치는 한번만 쓰인다
* 이웃해서 연속된 단어가 있는지 찾는다

* 백트래킹
* 모든 원소를 완전탐색하기 위한 목적으로 사용.
* 단순히 완전탐색하는 것이 아니라 조건에 따라서 유망한 노드로 이동.
*/
function exist(board: string[][], word: string): boolean {
  const m = board.length;
  const n = board[0].length;
  const l = word.length;
  const directions = [
    [-1, 0], // 상
    [1, 0], // 하
    [0, -1], // 좌
    [0, 1], // 우
  ];

  const backtrack = (
    col: number,
    row: number,
    idx: number,
    visited: Set<string>
  ): boolean => {
    if (idx === l) {
      return true;
    }
    if (
      col < 0 ||
      col >= m ||
      row < 0 ||
      row >= n ||
      board[col][row] !== word[idx] ||
      visited.has(`${col},${row}`)
    ) {
      return false;
    }

    visited.add(`${col},${row}`);

    for (const [dCol, dRow] of directions) {
      if (backtrack(col + dCol, row + dRow, idx + 1, visited)) {
        return true;
      }
    }

    visited.delete(`${col},${row}`);
    return false;
  };

  for (let col = 0; col < m; col++) {
    for (let row = 0; row < n; row++) {
      if (backtrack(col, row, 0, new Set<string>())) {
        return true;
      }
    }
  }
  return false;
}

// TC: O(m*n*4^l) <= m*n: 보드의 크기, l: 단어의 길이. 최대 4개 방향으로 이동 가능
// SC: O(l) <= 단어 길이만큼 방문 가능
