class TNode {
  isEndOf: boolean;
  children: Map<string, TNode>;

  constructor() {
    this.isEndOf = false;
    this.children = new Map<string, TNode>();
  }
}

class Trie {
  private root: TNode;

  constructor() {
    this.root = new TNode();
  }

  insert(word: string): void {
    let currentNode: TNode = this.root;

    for (const ch of word) {
      if (currentNode.children.has(ch)) {
        currentNode = currentNode.children.get(ch)!;
      } else {
        const newNode = new TNode();

        currentNode.children.set(ch, newNode);
        currentNode = currentNode.children.get(ch)!;
      }
    }
    currentNode.isEndOf = true;
  }

  search(word: string): boolean {
    let currentNode = this.root;

    for (const ch of word) {
      if (!currentNode.children.has(ch)) {
        return false;
      }

      currentNode = currentNode.children.get(ch)!;
    }

    return currentNode.isEndOf;
  }

  startsWith(prefix: string): boolean {
    let currentNode = this.root;

    for (const ch of prefix) {
      if (!currentNode.children.has(ch)) {
        return false;
      }

      currentNode = currentNode.children.get(ch)!;
    }

    return true;
  }
}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
