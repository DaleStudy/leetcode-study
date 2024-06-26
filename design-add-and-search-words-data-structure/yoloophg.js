// AddWord Method : Time Complexity: O(L)/Space Complexity: O(L)
// Search Method : Time Complexity: O(M)/Space Complexity: O(1)
// SearchInNode Method : Time Complexity: O(M)/Space Complexity: O(1)

var WordDictionary = function () {
  this.root = {};
};

WordDictionary.prototype.addWord = function (word) {
  // start from the root node
  let node = this.root;
  for (let char of word) {
    if (!node[char]) {
      // if the character does not exist, create a new node
      node[char] = {};
    }
    // move to the next node
    node = node[char];
  }
  // mark the end of the word
  node.isEndOfWord = true;
};

WordDictionary.prototype.search = function (word) {
  // start searching from the root
  return this.searchInNode(word, 0, this.root);
};

WordDictionary.prototype.searchInNode = function (word, index, node) {
  if (index === word.length) {
    // if all characters are checked
    return node.isEndOfWord === true;
  }

  const char = word[index];
  if (char === ".") {
    //iIf the character is '.', check all possible nodes at this part
    for (let key in node) {
      if (
        key !== "isEndOfWord" &&
        this.searchInNode(word, index + 1, node[key])
      ) {
        // if any path matches, return true
        return true;
      }
    }
    // no path matched
    return false;
  } else if (node[char]) {
    // if the character exists in the trie
    return this.searchInNode(word, index + 1, node[char]);
  } else {
    // character path does not exist
    return false;
  }
};
