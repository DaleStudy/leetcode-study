// Time Complexity: O(n)

class TrieNode {
  children: { [key: string]: TrieNode };
  ending: boolean;

  constructor(ending = false) {
    this.children = {};
    this.ending = ending;
  }
}

class Trie {
  root: TrieNode;

  constructor() {
    this.root = new TrieNode();
  }

  insert(word: string): void {
    let node = this.root;

    for (const ch of word) {
      if (!(ch in node.children)) {
        node.children[ch] = new TrieNode();
      }
      node = node.children[ch];
    }
    node.ending = true;
  }

  search(word: string): boolean {
    let node = this.root;

    for (const ch of word) {
      if (!(ch in node.children)) {
        return false;
      }
      node = node.children[ch];
    }
    return node.ending;
  }

  startsWith(prefix: string): boolean {
    let node = this.root;

    for (const ch of prefix) {
      if (!(ch in node.children)) {
        return false;
      }

      node = node.children[ch];
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
