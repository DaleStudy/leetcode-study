function TrieNode() {
  this.children = {};
  this.isEnd = false;
}

function Trie() {
  this.root = new TrieNode();
}

Trie.prototype.insert = function (word) {
  let node = this.root;
  for (let char of word) {
    if (!node.children[char]) {
      node.children[char] = new TrieNode();
    }
    node = node.children[char];
  }
  node.isEnd = true;
};

Trie.prototype.search = function (word) {
  let node = this._traverse(word);
  return node !== null && node.isEnd === true;
};

Trie.prototype.startsWith = function (prefix) {
  return this._traverse(prefix) !== null;
};

Trie.prototype._traverse = function (str) {
  let node = this.root;
  for (let char of str) {
    if (!node.children[char]) return null;
    node = node.children[char];
  }
  return node;
};
