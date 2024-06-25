// Insert Method : Time Complexity: O(m)/Space Complexity: O(m)
// Search Method : Time Complexity: O(m)/Space Complexity: O(1)
// Starts With Method : Time Complexity: O(p)/Space Complexity: O(1)

var Trie = function () {
  this.trie = {};
};

// insert a word into the Trie
Trie.prototype.insert = function (word) {
  let node = this.trie;
  for (let char of word) {
    if (!node[char]) {
      // create a new node if it doesn't exist
      node[char] = {};
    }
    // move to the next node
    node = node[char];
  }
  // mark the end of the word
  node.isEnd = true;
};

// search for a word in the Trie
Trie.prototype.search = function (word) {
  let node = this.trie;
  for (let char of word) {
    if (!node[char]) {
      // character not found
      return false;
    }
    // move to the next node
    node = node[char];
  }
  // Ccheck if it's the end of a valid word
  return node.isEnd === true;
};

// check if there's any word in the Trie that starts with the given prefix
Trie.prototype.startsWith = function (prefix) {
  let node = this.trie;
  for (let char of prefix) {
    if (!node[char]) {
      // prefix not found
      return false;
    }
    // move to the next node
    node = node[char];
  }
  // prefix found
  return true;
};
