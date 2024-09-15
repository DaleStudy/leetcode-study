/**
 * https://leetcode.com/problems/implement-trie-prefix-tree
 */
class Trie {
  constructor(private root: Record<string, any> = {}) {}

  insert(word: string): void {
    let node = this.root;
    for (const char of word) {
      if (!node[char]) {
        node[char] = {};
      }
      node = node[char];
    }
    node.isEnd = true;
  }

  search(word: string): boolean {
    let node = this.root;
    for (const char of word) {
      if (!node[char]) {
        return false;
      }
      node = node[char];
    }
    return !!node.isEnd;
  }

  startsWith(prefix: string): boolean {
    let node = this.root;
    for (const char of prefix) {
      if (!node[char]) {
        return false;
      }
      node = node[char];
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
