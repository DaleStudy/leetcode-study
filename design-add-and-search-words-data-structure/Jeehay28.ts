class WordDictionary {
  root: {
    [key: string]: any;
  };

  constructor() {
    this.root = { $: true }; // ending
  }

  // {
  //   "$": true,
  //   "b": {
  //     "$": false,
  //     "a": {
  //       "$": false,
  //       "d": {
  //         "$": true
  //       }
  //     }
  //   }
  // }

  // TC: O(w)
  // SC: O(w)
  addWord(word: string): void {
    let node = this.root;

    for (const ch of word) {
      if (!node[ch]) {
        node[ch] = { $: false };
      }
      node = node[ch];
    }

    node["$"] = true;
  }

  // TC: O(26^w)
  // SC: O(w)
  search(word: string): boolean {
    const dfs = (node, idx: number) => {
      if (idx === word.length) {
        return node["$"];
      }

      const ch = word[idx];

      if (node[ch]) {
        return dfs(node[ch], idx + 1);
      }

      if (ch === ".") {
        for (const key of Object.keys(node)) {
          if (key !== "$" && dfs(node[key], idx + 1)) {
            return true;
          }
        }
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

