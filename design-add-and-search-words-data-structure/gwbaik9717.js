var Node = function () {
  this.children = new Map();
  this.isEnd = false;
};

var WordDictionary = function () {
  this.root = new Node();
};

/**
 * @param {string} word
 * @return {void}
 */
WordDictionary.prototype.addWord = function (word) {
  let current = this.root;

  for (const chr of word) {
    if (!current.children.has(chr)) {
      current.children.set(chr, new Node());
    }

    current = current.children.get(chr);
  }

  current.isEnd = true;
};

/**
 * @param {string} word
 * @return {boolean}
 */
WordDictionary.prototype.search = function (word) {
  const stack = [[0, this.root]];

  while (stack.length > 0) {
    const [index, currentNode] = stack.pop();

    if (index === word.length) {
      if (currentNode.isEnd) {
        return true;
      }

      continue;
    }

    if (word[index] === ".") {
      for (const [_, child] of currentNode.children) {
        stack.push([index + 1, child]);
      }

      continue;
    }

    if (currentNode.children.has(word[index])) {
      stack.push([index + 1, currentNode.children.get(word[index])]);
    }
  }

  return false;
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
