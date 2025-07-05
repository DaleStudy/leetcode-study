/*
L : 평균 단어 길이
Time Complexity: O(M * N * 4^L)
Space Complexity: O(∑L + M × N)
*/
class TrieNode {
    children: Map<string, TrieNode>
    word: string | null

    constructor() {
        this.children = new Map()
        this.word = null
    }
}

class Trie {
    root: TrieNode
    constructor() {
        this.root = new TrieNode()
    }

    insert(word: string): void {
        let node = this.root

        for (const char of word) {
            if (!node.children.has(char)) {
                node.children.set(char, new TrieNode())
            }
            node = node.children.get(char)
        }
        node.word = word
    }
}

function dfs(board: string[][], row: number, col: number, node: TrieNode, visited: boolean[][], result: string[]): void {
        const rows = board.length
        const cols = board[0].length
        if (row < 0 || row >= board.length || 
            col < 0 || col >= board[0].length || 
            visited[row][col]) {
            return
        }
        const char = board[row][col]
        if (!node.children.has(char)) {
            return
        }
        node = node.children.get(char)!

        if (node.word !== null) {
            result.push(node.word)
            node.word = null
        }
        const originalChar = board[row][col]
        visited[row][col] = true
        const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for (const [dr, dc] of directions) {
            dfs(board, row + dr, col + dc, node, visited, result)
        }
        visited[row][col] = false
    } 

function findWords(board: string[][], words: string[]): string[] {
    if (!board || board.length === 0 || !board[0] || board[0].length === 0) {
        return []
    }
   const result: string[] = []
   const trie = new Trie()

    for (const word of words) {
        trie.insert(word)
    }

    const rows = board.length
    const cols = board[0].length
    const visited = Array(rows).fill(null).map(() => Array(cols).fill(false))

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            dfs(board, i, j, trie.root, visited, result)
        }
    }
    return result
};
