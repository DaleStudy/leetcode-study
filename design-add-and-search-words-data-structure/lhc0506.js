const Node = function() {
    this.children = {};
    this.isEnd = false;
}

var WordDictionary = function() {
    this.root = new Node();
};

/**
 * @param {string} word
 * @return {void}
 */
WordDictionary.prototype.addWord = function(word) {
    let currentNode = this.root;

    for (let char of word) {
        if (!currentNode.children[char]) {
            currentNode.children[char] = new Node();
        }
        currentNode = currentNode.children[char];
    }

    currentNode.isEnd = true;
};

/**
 * @param {string} word
 * @return {boolean}
 */
WordDictionary.prototype.search = function(word) {
    if (word === undefined) return false;
    return this._search(this.root, word, 0);
};

WordDictionary.prototype._search = function(node, word, index) {
    if (index === word.length) {
        return node.isEnd;
    }

    const char = word[index];

    if (char !== '.') {
        const child = node.children[char];
        return child ? this._search(child, word, index + 1) : false;
    }

    for (const key in node.children) {
        if (this._search(node.children[key], word, index + 1)) {
            return true;
        }
    }

    return false;
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */

// n: 단어수, m: 단어 길이
// addWord: 시간 복잡도 O(m)
// search: 	시간 복잡도 O(m)
// 공간 복잡도 O(n * m)
