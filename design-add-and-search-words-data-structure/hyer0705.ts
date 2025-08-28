class TNode {
  isEndOf: boolean;
  children: Map<string, TNode>;

  constructor() {
    this.isEndOf = false;
    this.children = new Map<string, TNode>();
  }
}

class WordDictionary {
  private root: TNode;

  constructor() {
    this.root = new TNode();
  }

  addWord(word: string): void {
    let current = this.root;

    for (const ch of word) {
      if (!current.children.has(ch)) {
        current.children.set(ch, new TNode());
      }

      current = current.children.get(ch)!;
    }

    current.isEndOf = true;
  }

  search(word: string): boolean {
    const find = (node: TNode, index: number): boolean => {
      if (index === word.length) {
        if (node.isEndOf) return true;
        return false;
      }

      const currentCh = word[index];

      if (currentCh === ".") {
        for (const [ch, child] of node.children) {
          if (find(child, index + 1)) return true;
        }

        return false;
      } else {
        const child = node.children.get(currentCh);
        if (child) {
          return find(child, index + 1);
        }

        return false;
      }

      return false;
    };

    return find(this.root, 0);
  }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
