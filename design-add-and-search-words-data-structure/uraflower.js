class TrieNode {
    constructor(value) {
        this.value = value;
        this.children = {};
        this.end = false;
    }
}

class WordDictionary {
    constructor() {
        this.root = new TrieNode(null);
    }

    /** 
     * 시간복잡도: O(w) (w: word.length)
     * 공간복잡도: O(w)
     * @param {string} word
     * @return {void}
     */
    addWord(word) {
        let current = this.root;

        for (const char of word) {
            if (!current.children[char]) {
                const child = new TrieNode(char);
                current.children[char] = child;
            }
            current = current.children[char];
        }

        current.end = true;
    };

    /** 
     * 시간복잡도: O(k * w) (k: children의 길이로 최대 26, w: word.length)
     * 공간복잡도: O(w)
     * @param {string} word
     * @return {boolean}
     */
    search(word) {
        return this.#search(this.root, word, 0);
    };

    #search(node, word, idx) {
        if (!node) return false;
        if (idx >= word.length) return node.end;

        if (word[idx] === '.') {
            for (const current of Object.values(node.children)) {
                if (this.#search(current, word, idx + 1)) {
                    return true;
                }
            }
            return false;
        } else {
            return this.#search(node.children[word[idx]], word, idx + 1);
        }
    }
};
