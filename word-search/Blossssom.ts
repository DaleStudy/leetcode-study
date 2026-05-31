/**
 * @param board - m * n 문자 그리드
 * @param word - 찾을 단어
 * @returns - 그리드 내 인접한 셀의 글자로 word를 만들 수 있는지 반환
 * @description
 * - 동일한 셀 글자는 한 번만 사용가능
 * - visit 체크 부분에서 조금 생각을 잘못해 오래걸림
 * - dfs 연습 필요, 문제를 최대한 잘게 잘라서 생각해보기
 */

function exist(board: string[][], word: string): boolean {
  const maximumRow = board.length - 1;
  const maximumCol = board[0].length - 1;
  // 시작지점 찾기
  const starter = board.reduce<number[][]>((acc, row, rIndex) => {
    row.forEach((col, cIndex) => {
      if (col === word[0]) {
        acc.push([rIndex, cIndex]);
      }
    });
    return acc;
  }, []);

  function recursive(row: number, col: number, target: number): boolean {
    // word의 길이까지 왔다면 이전 조건은 통과 즉, word와 동일 문자열
    if (target === word.length) {
      return true;
    }

    // 인접 index 범위 체크 및 값 체크
    if (
      row < 0 ||
      row > maximumRow ||
      col < 0 ||
      col > maximumCol ||
      board[row][col] !== word[target]
    ) {
      return false;
    }
    // 이전 값을 동일 체크하지 않도록 값을 저장 및 변경
    const saveValue = board[row][col];
    // 찡긋
    board[row][col] = ">_o";

    const finding =
      recursive(row + 1, col, target + 1) ||
      recursive(row - 1, col, target + 1) ||
      recursive(row, col + 1, target + 1) ||
      recursive(row, col - 1, target + 1);

    // 다음 순회 및 체크를 위한 원상복구
    board[row][col] = saveValue;
    return finding;
  }

  for (const start of starter) {
    const isFind = recursive(start[0], start[1], 0);
    if (isFind) {
      return true;
    }
  }
  return false;
}

const board = [
  ["A", "B", "C", "E"],
  ["S", "F", "C", "S"],
  ["A", "D", "E", "E"],
];

const word = "ABCCED";
console.log(exist(board, word));

