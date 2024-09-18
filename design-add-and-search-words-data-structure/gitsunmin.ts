/**
 * https://leetcode.com/problems/design-add-and-search-words-data-structure
 * n: The total number of words stored in the Trie.
 * m: The average length of each word.
 * 
 * time complexity:
 * - addWord: O(m)
 * - search: O(26^m) in the worst case (with multiple wildcards) to O(m) in general cases.
 * space complexity: O(n * m)
 */
class TrieNode {
    children: Map<string, TrieNode>;
    isEnd: boolean;

    constructor() {
        this.children = new Map();
        this.isEnd = false;
    }
}

export class WordDictionary {
    private root: TrieNode;

    constructor() {
        this.root = new TrieNode();
    }

    addWord(word: string): void {
        let node = this.root;

        for (const char of word) {
            if (!node.children.has(char)) node.children.set(char, new TrieNode());

            node = node.children.get(char)!;
        }
        node.isEnd = true;
    }

    search(word: string): boolean {
        return this.searchInNode(word, 0, this.root);
    }

    private searchInNode(word: string, index: number, node: TrieNode): boolean {
        if (index === word.length) return node.isEnd;

        const char = word[index];

        if (char === '.') {
            for (const child of node.children.values()) {
                if (this.searchInNode(word, index + 1, child)) return true;
            }
            return false;
        } else {
            if (!node.children.has(char)) return false;
            return this.searchInNode(word, index + 1, node.children.get(char)!);
        }
    }
}
