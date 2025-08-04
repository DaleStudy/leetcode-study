class TrieNode {
    constructor() {
        this.children = {};
        this.isWord = false;
    }

    add(word) {
        let node = this;
        for (let ch of word) {
            if (!node.children[ch]) {
                node.children[ch] = new TrieNode();
            }
            node = node.children[ch];
        }
        node.isWord = true;
    }
}

/**
 * @param {character[][]} board
 * @param {string[]} words
 * @return {string[]}
 */
var findWords = function(board, words) {
    const root = new TrieNode();
    for (let word of words) {
        root.add(word);
    }

    const ROWS = board.length;
    const COLS = board[0].length;
    const res = new Set();
    const visit = new Set();

    const dfs = (r, c, node, word) => {
        if (
            r < 0 || c < 0 ||
            r >= ROWS || c >= COLS ||
            visit.has(`${r},${c}`) ||
            !node.children[board[r][c]]
        ) return;

        visit.add(`${r},${c}`);
        node = node.children[board[r][c]];
        word += board[r][c];

        if (node.isWord) {
            res.add(word);
        }

        dfs(r + 1, c, node, word);
        dfs(r - 1, c, node, word);
        dfs(r, c + 1, node, word);
        dfs(r, c - 1, node, word);

        visit.delete(`${r},${c}`);
    };

    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            dfs(r, c, root, "");
        }
    }

    return Array.from(res);
};

