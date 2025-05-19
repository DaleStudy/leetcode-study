
var Trie = function() {
    this.isEnd = false;
};

/**
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    let currentTrie = this;
    word.split('').forEach(alphabet => {
        if (!currentTrie[alphabet]) {
            currentTrie[alphabet] = new Trie();
        }
        currentTrie = currentTrie[alphabet];
    });

    currentTrie.isEnd = true;
};

/**
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    let currentTrie = this;

    for (let alphabet of word) {
        if (!currentTrie[alphabet]) {
            return false;
        }
        currentTrie = currentTrie[alphabet];
    }

    return currentTrie.isEnd;
};

/**
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    let currentTrie = this;

    for (let alphabet of prefix) {
        if (!currentTrie[alphabet]) {
            return false;
        }
        currentTrie = currentTrie[alphabet];
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


// insert 시간복잡도: O(n), search 시간복잡도: O(n), startsWith 시간복잡도: O(n)
