class WordDictionary {
  root: Record<string, any>;

  constructor() {
    this.root = { $: true };
  }

  addWord(word: string): void {
    let node = this.root;
    for (const ch of word) {
      if (!(ch in node)) {
        node[ch] = { $: false };
      }
      node = node[ch];
    }
    node["$"] = true;
  }

  search(word: string): boolean {
    const dfs = (node: Record<string, any>, idx: number): boolean => {
      if (idx === word.length) return node["$"];

      const ch = word[idx];
      if (ch === ".") {
        for (const key in node) {
          if (key !== "$" && dfs(node[key], idx + 1)) {
            return true;
          }
        }
        return false;
      }

      if (ch in node) {
        return dfs(node[ch], idx + 1);
      }

      return false;
    };
    return dfs(this.root, 0);
  }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
