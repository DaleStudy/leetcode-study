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
WordDictionary.prototype.search = function (word) {
  if (word.indexOf(".") != -1) {
    // Case of word has a '.'
    for (let str of this.dictionary) {
      if (str.length != word.length) continue;
      let i;
      for (i = 0; i < word.length; i++) {
        if (word[i] === ".") continue;
        if (word[i] != str[i]) break;
      }
      if (i === str.length) return true;
    }
    return false;
  } else {
    return this.dictionary.has(word);
  }
};

// n: number of words | m: length of the word
// TC: O(n*m)
// SC: O(n*m)
