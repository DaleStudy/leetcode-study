// 모든 word에 대해
// board를 순회하면서
// word의 첫 글자가 board의 현 위치 문자와 같다면 dfs
// 이렇게 풀 경우 O(W * m * n * 4^L)만큼 시간이 걸림 (W: words.length, L: word.length)

// 그래서 모든 word를 트라이로 저장하고
// board를 한 번만 순회하는 방법을 사용

const buildTrie = (words) => {
    const root = {};

    for (const word of words) {
        let node = root;
        for (const char of word) {
            if (!node[char]) node[char] = {};
            node = node[char];
        }
        node.word = word;
    }

    return root;
}

/**
 * @param {character[][]} board
 * @param {string[]} words
 * @return {string[]}
 */
const findWords = function (board, words) {
    const m = board.length;
    const n = board[0].length;
    const trie = buildTrie(words);
    const result = [];

    const dr = [0, 0, 1, -1];
    const dc = [1, -1, 0, 0];
    const visited = Array.from({ length: m }).map(() => Array.from({ length: n }).fill(false));

    const dfs = (r, c, node, path) => {
        const char = board[r][c];
        const nextNode = node[char];
        if (!nextNode) return;

        if (nextNode.word) {
            result.push(nextNode.word);
            nextNode.word = null;
        }

        visited[r][c] = true;

        for (let i = 0; i < 4; i++) {
            const nr = r + dr[i];
            const nc = c + dc[i];

            if (0 <= nr && nr < m && 0 <= nc && nc < n && !visited[nr][nc]) {
                dfs(nr, nc, nextNode, path + board[nr][nc]);
            }
        }

        visited[r][c] = false;
    }

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            dfs(i, j, trie, '');
        }
    }

    return result;
};

// 시간복잡도: O(m * n * 4^L) (L: word.length)
// 공간복잡도: O(W * L + m * n)
//  - trie: O(W * L) (W: words.length)
//  - vistied: O(m * n)
//  - 재귀스택: O(L)
//  - result: O(K * L) (K: 찾은 단어 수)
