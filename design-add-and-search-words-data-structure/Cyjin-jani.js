var WordDictionary = function () {
  this.dictionary = new Set();
};

/**
 * @param {string} word
 * @return {void}
 */
WordDictionary.prototype.addWord = function (word) {
  this.dictionary.add(word);
};

/**
 * @param {string} word
 * @return {boolean}
 */

// tc:  O(n * k), n: dictionary size, k: word length => O(n) in worst case
// sc: O(1)
WordDictionary.prototype.search = function (word) {
  if (!word.includes('.')) {
    return this.dictionary.has(word);
  }

  for (const stored of this.dictionary) {
    if (stored.length !== word.length) continue;

    let isMatch = true;
    for (let i = 0; i < word.length; i++) {
      if (word[i] === '.') continue;
      if (word[i] !== stored[i]) {
        isMatch = false;
        break;
      }
    }
    if (isMatch) return true;
  }

  return false;
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
