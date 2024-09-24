class WordDictionary {
  wordCountMap: Map<number, Set<string>>;
  constructor() {
    this.wordCountMap = new Map();
  }

  // TC: O(1)
  // SC: O(n)
  addWord(word: string): void {
    const length = word.length;
    if (this.wordCountMap.has(length)) {
      this.wordCountMap.get(length).add(word);
    } else {
      this.wordCountMap.set(length, new Set([word]));
    }
    return null;
  }

  // TC: O(m*n) // m: words length, n: word length
  // SC: O(n)
  search(word: string): boolean {
    const len = word.length;
    const targetWord = word.replace(/\./g, "");
    const hasDot = len - targetWord.length !== 0;

    if (!this.wordCountMap.has(len)) {
      return false;
    }
    const words = this.wordCountMap.get(len);
    if (!hasDot) {
      return words.has(word);
    }

    for (const w of words) {
      let match = true;
      for (let j = 0; j < w.length; j++) {
        if (word[j] !== "." && word[j] !== w[j]) {
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
