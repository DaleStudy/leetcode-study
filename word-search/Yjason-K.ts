/**
 * board 에서 주어진 단어를 찾을 수 있는지 여부 확인 (boolean)
 * @param {string[][]} board - 단어를 탐색할 2D board
 * @param {string} word - 찾고자 하는 단어
 * @returns {boolean} - 단어가 격자에서 존재하면 true, 그렇지 않으면 false
 * 
 * 시간 복잡도: O(N * M * 4^L)
 * - N: board의 행 개수
 * - M: board의 열 개수
 * - L: word의 길이
 * 
 * 공간 복잡도: O(L) (재귀 호출 스택)
 */
function exist(board: string[][], word: string): boolean {
    const rows = board.length;
    const cols = board[0].length;

    // 방향 배열 (상, 하, 좌, 우)
    const directions = [
        [0, -1], // 상
        [0, 1],  // 하
        [-1, 0], // 좌
        [1, 0],  // 우
    ];

    /**
     * DFS 탐색(깊이 우선 탐색)을 통해 단어를 찾는 함수
     * @param {number} x - 현재 x 좌표 (열)
     * @param {number} y - 현재 y 좌표 (행)
     * @param {number} index - 현재 탐색 중인 word의 문자 인덱스
     * @returns {boolean} - 현재 경로가 유효하면 true, 유효하지 않으면 false
     */
    const dfs = (x: number, y: number, index: number): boolean => {
        // 단어를 모두 찾았을 경우
        if (index === word.length) return true;

        // 범위를 벗어나거나 문자가 일치하지 않는 경우
        if (x < 0 || y < 0 || x >= cols || y >= rows || board[y][x] !== word[index]) {
            return false;
        }

        // 현재 위치 방문 처리 (임시 수정)
        const temp = board[y][x];
        board[y][x] = "#";

        // 상하좌우 탐색
        for (const [dx, dy] of directions) {
            if (dfs(x + dx, y + dy, index + 1)) {
                return true;
            }
        }

        // 백트래킹: 셀 값 복구
        board[y][x] = temp;

        return false;
    };

    // board에서 word 첫글자가 일치하는 경우 탐색 시작
    for (let y = 0; y < rows; y++) {
        for (let x = 0; x < cols; x++) {
            if (board[y][x] === word[0] && dfs(x, y, 0)) {
                return true;
            }
        }
    }

    return false;
}

