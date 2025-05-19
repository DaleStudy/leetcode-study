var Trie = function() {
    this.root = {}; // 루트는 빈 객체로 시작
};

/** 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    let node = this.root;
    for (let ch of word) {
        if (!node[ch]) node[ch] = {};
        node = node[ch];
    }
    node.isEnd = true; // 단어의 끝을 표시
};

/** 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    let node = this.root;
    for (let ch of word) {
        if (!node[ch]) return false;
        node = node[ch];
    }
    return node.isEnd === true; // 단어의 끝이어야만 true
};

/** 
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    let node = this.root;
    for (let ch of prefix) {
        if (!node[ch]) return false;
        node = node[ch];
    }
    return true; // 접두사만 매칭되면 true
};
