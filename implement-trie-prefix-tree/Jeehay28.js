// Space complexity: O(n * m), where n is the number of words and m is the average length of the words stored in the trie.
var Trie = function () {
  this.root = {}; // Initialize the trie with a root node
};

/**
 * @param {string} word
 * @return {void}
 */

// Time Complexity: O(m), where m is the length of the word being inserted
Trie.prototype.insert = function (word) {
  let currentNode = this.root;
  for (any of word) {
    // If the character doesn't exist, create a new node
    if (!currentNode[any]) {
      currentNode[any] = {};
    }
    currentNode = currentNode[any]; // Move to the next node
  }
  currentNode.end = true; // Mark the end of the word
};

/**
 * @param {string} word
 * @return {boolean}
 */
// Time Complexity: O(m), where m is the length of the word being searched
Trie.prototype.search = function (word) {
  let currentNode = this.root;
  for (any of word) {
    // If the character doesn't exist in the trie, return false
    if (!currentNode[any]) {
      return false;
    }
    currentNode = currentNode[any]; // Move to the next node
  }

  return currentNode.end === true;
};

/**
 * @param {string} prefix
 * @return {boolean}
 */
// Time Complexity: O(m), where m is the length of the prefix
Trie.prototype.startsWith = function (prefix) {
  let currentNode = this.root;

  for (any of prefix) {
    // If the character doesn't exist, return false
    if (!currentNode[any]) {
      return false;
    }
    currentNode = currentNode[any]; // Move to the next node
  }

  return true; // Return true if the prefix exists
};

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */


