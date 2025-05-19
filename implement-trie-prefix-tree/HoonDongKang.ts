/**
 * [Problem]: [208] Implement Trie (Prefix Tree)
 * (https://leetcode.com/problems/implement-trie-prefix-tree/description/)
 */

class TrieNode {
    children: { [key: string]: TrieNode };
    isEnd: boolean;

    constructor() {
        this.children = {};
        this.isEnd = false;
    }
}

class Trie {
    constructor(private root = new TrieNode()) {}

    //시간복잡도: O(n)
    //공간복잡도: O(n)
    insert(word: string): void {
        let node = this.root;
        for (let char of word) {
            if (!node.children[char]) {
                node.children[char] = new TrieNode();
            }

            node = node.children[char];
        }

        node.isEnd = true;
    }

    //시간복잡도: O(n)
    //공간복잡도: O(n)
    search(word: string): boolean {
        let node = this.root;
        for (let char of word) {
            if (!node.children[char]) return false;
            node = node.children[char];
        }

        return node.isEnd;
    }

    //시간복잡도: O(n)
    //공간복잡도: O(n)
    startsWith(prefix: string): boolean {
        let node = this.root;
        for (let char of prefix) {
            if (!node.children[char]) return false;
            node = node.children[char];
        }

        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
