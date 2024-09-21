/**
 * https://leetcode.com/problems/design-add-and-search-words-data-structure
 */
// Using Trie
class WordDictionary {
  constructor(private root: Record<string, any> = {}) {}

  /**
   * T.C. O(L) L: length of a word
   * S.C. O(L)
   */
  addWord(word: string): void {
    let node = this.root;
    for (const char of word) {
      if (!node[char]) {
        node[char] = {};
      }
      node = node[char];
    }
    node['isEnd'] = true;
  }

  /**
   * T.C. O(N) - there are only 2 dots in the word(26 * 26 * N)
   * S.C. O(N * L) N: number of words, L: length of a word
   */
  search(word: string): boolean {
    return this.dfs(word, this.root);
  }

  private dfs(word: string, node: Record<string, any>): boolean {
    for (let i = 0; i < word.length; i++) {
      if (word[i] === '.') {
        for (const key in node) {
          if (this.dfs(word.slice(i + 1), node[key])) {
            return true;
          }
        }
        return false;
      }
      if (!node[word[i]]) {
        return false;
      }
      node = node[word[i]];
    }
    return !!node['isEnd'];
  }
}

// Using Array and Set
class WordDictionary {
  constructor(
    private words: Set<string>[] = Array.from({ length: 25 }, () => new Set())
  ) {}

  /**
   * T.C. O(1)
   * S.C. O(N * L)
   */
  addWord(word: string): void {
    this.words[word.length - 1].add(word);
  }

  /**
   * T.C. O(N * L) N: number of words, L: length of a word
   * S.C. O(1)
   */
  search(word: string): boolean {
    const hasDot = word.indexOf('.') !== -1;
    const set = this.words[word.length - 1];

    if (!hasDot) {
      return set.has(word);
    }

    for (const w of set) {
      let i = 0;
      while (i < word.length) {
        if (word[i] == '.') {
          i++;
          continue;
        }
        if (word[i] !== w[i]) {
          break;
        }
        i++;
      }

      if (i === word.length) {
        return true;
      }
    }
    return false;
  }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
