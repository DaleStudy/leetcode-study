// 시간복잡도
// insert: O(L), search: O(L), startsWith: O(L)
// 공간복잡도: O(N * L)

var TrieNode = function(){
    this.children = {};
    this.endOfWord = false;
}

var Trie = function() {
    this.root = new TrieNode();
};

/**
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    let curNode = this.root;
    for (let i = 0; i < word.length; i++) {
        const char = word[i];
        if (!curNode.children[char]) {
            curNode.children[char] = new TrieNode();
        }
        curNode = curNode.children[char];
    }
    curNode.endOfWord = true;
};

/**
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    let curNode = this.root;
    for (let i = 0; i < word.length; i++) {
        const char = word[i];
        if (!curNode.children[char]) {
            return false;
        }
        curNode = curNode.children[char];
    }
    return curNode.endOfWord;
};

/**
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    let curNode = this.root;
    for (let i = 0; i < prefix.length; i++) {
        const char = prefix[i];
        if (!curNode.children[char]) {
            return false;
        }
        curNode = curNode.children[char];
    }
    return true;
};
