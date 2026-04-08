// 문제풀이 해설 보고 푼 문제입니다.

var TrieNode = function () {
    this.children = {};
    this.isEnd = false;
}

var Trie = function () {
    this.root = new TrieNode();
};

/** 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function (word) {
    let currentNode = this.root;
    for (let i = 0; i < word.length; i++) {
        let char = word[i];
        if (!currentNode.children[char]) {
            currentNode.children[char] = new TrieNode();

        }
        currentNode = currentNode.children[char];
    }

    currentNode.isEnd = true;
};

/** 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function (word) {
    let currentNode = this.root;
    for (let i = 0; i < word.length; i++) {
        let char = word[i];
        if (!currentNode.children[char]) {
            return false;
        }
        currentNode = currentNode.children[char];
    }
    return currentNode.isEnd;
};

/** 
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function (prefix) {
    let currentNode = this.root;
    for (let i = 0; i < prefix.length; i++) {
        let char = prefix[i];
        if (!currentNode.children[char]) {
            return false;
        }
        currentNode = currentNode.children[char];
    }
    return true;
};

/** 
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
