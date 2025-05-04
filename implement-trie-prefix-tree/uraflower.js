const Node = function (value) {
    this.value = value;
    this.children = {};
    this.data = null;
}

const Trie = function () {
    this.root = new Node(null);
};

/** 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function (word) {
    let parent = this.root;

    for (let i = 0; i < word.length; i++) {
        if (!parent.children[word[i]]) {
            parent.children[word[i]] = new Node(word[i]);
        }
        parent = parent.children[word[i]];
    }

    parent.data = word;
};

/** 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function (word) {
    let parent = this.root;
    let i = 0;

    while (i < word.length && parent.children[word[i]]) {
        parent = parent.children[word[i]];
        i += 1;
    }

    return parent.data === word;
};

/** 
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function (prefix) {
    let parent = this.root;

    for (let char of prefix) {
        if (!parent.children[char]) return false;
        parent = parent.children[char];
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
