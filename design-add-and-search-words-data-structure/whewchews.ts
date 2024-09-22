class WordDictionary {
  wordList: Set<string>;
  wordCountMap: Map<number, string[]>;
  constructor() {
    this.wordList = new Set();
    this.wordCountMap = new Map();
  }

  // TC: O(1)
  // SC: O(n)
  addWord(word: string): void {
    this.wordList.add(word);
    const length = word.length;
    if (this.wordCountMap.has(length)) {
      this.wordCountMap.get(length).push(word);
    } else {
      this.wordCountMap.set(length, [word]);
    }
    return null;
  }

  // TC: O(m*n) // m: words length, n: word length
  // SC: O(n)
  search(word: string): boolean {
    const len = word.length;
    const targetWord = word.replace(/\./g, "");
    const hasDot = len - targetWord.length !== 0;

    if (!hasDot) return this.wordList.has(word);
    if (!this.wordCountMap.has(len)) {
      return false;
    }
    const words = this.wordCountMap.get(len);
    for (let i = 0; i < words.length; i++) {
      let match = true;
      for (let j = 0; j < words[i].length; j++) {
        if (word[j] !== "." && word[j] !== words[i][j]) {
          match = false;
          break;
        }
      }
      if (match) {
        return true;
      }
    }
    return false;
  }
}
