const TrieNode = function () {
  this.children = {};
  this.isEndOfWord = false;
};
var WordDictionary = function () {
  this.root = new TrieNode();
};

/**
 * @param {string} word
 * @return {void}
 */
WordDictionary.prototype.addWord = function (word) {
  let currentNode = this.root;
  for (let i = 0; i < word.length; i++) {
    let char = word[i];
    if (!currentNode.children[char]) {
      currentNode.children[char] = new TrieNode();
    }
    currentNode = currentNode.children[char];
  }
  currentNode.isEndOfWord = true;
};

/**
 * @param {string} word
 * @return {boolean}
 */
WordDictionary.prototype.search = function (word) {};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
