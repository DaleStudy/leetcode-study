/**
 * [Problem]: [212] Word Search II
 * (https://leetcode.com/problems/word-search-ii/)
 */

class TrieNode {
    children: Map<string, TrieNode> = new Map();
    word: string | null = null;
}

//시간복잡도 O(m * n * 4^s)
//공간복잡도 O(trie 저장 공간(word * length) + result)
function findWords(board: string[][], words: string[]): string[] {
    const result: string[] = [];
    const rows = board.length;
    const cols = board[0].length;

    const root = new TrieNode();
    for (const word of words) {
        let node = root;

        for (const char of word) {
            if (!node.children.has(char)) {
                node.children.set(char, new TrieNode());
            }
            node = node.children.get(char)!;
        }

        node.word = word;
    }

    const dfs = (i: number, j: number, node: TrieNode) => {
        const char = board[i][j];
        const next = node.children.get(char);
        if (!next) return;

        if (next.word) {
            result.push(next.word);
            next.word = null;
        }

        board[i][j] = "#";

        const directions = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0],
        ];

        for (const [dx, dy] of directions) {
            const ni = i + dx;
            const nj = j + dy;

            if (ni >= 0 && ni < rows && nj >= 0 && nj < cols && board[ni][nj] !== "#") {
                dfs(ni, nj, next);
            }
        }

        board[i][j] = char;

        if (next.children.size === 0) {
            node.children.delete(char);
        }
    };

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            dfs(i, j, root);
        }
    }

    return result;
}
