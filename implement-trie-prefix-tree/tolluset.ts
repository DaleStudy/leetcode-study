class TrieNode {
  public children: Map<string, TrieNode>;
  public isEnd: boolean;

  constructor() {
    this.children = new Map();
    this.isEnd = false;
  }
}

class Trie {
  private root: TrieNode;

  constructor() {
    this.root = new TrieNode();
  }

  /**
   * TC: O(n)
   * SC: O(n)
   * */
  insert(word: string): void {
    let node = this.root;

    for (const char of word) {
      if (!node.children.has(char)) {
        node.children.set(char, new TrieNode());
      }

      node = node.children.get(char)!;
    }

    node.isEnd = true;
  }

  /**
   * TC: O(n)
   * SC: O(1)
   * */
  search(word: string): boolean {
    let node = this.root;

    for (const char of word) {
      if (!node.children.has(char)) {
        return false;
      }

      node = node.children.get(char)!;
    }

    return node.isEnd;
  }

  /**
   * TC: O(n)
   * SC: O(1)
   * */
  startsWith(prefix: string): boolean {
    let node = this.root;

    for (const char of prefix) {
      if (!node.children.has(char)) {
        return false;
      }

      node = node.children.get(char)!;
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

const trie = new Trie();

trie.insert("apple");

const tc1 = trie.search("apple"); // return True
console.info("🚀 : tolluset.ts:59: tc1=", tc1);

const tc2 = trie.search("app"); // return False
console.info("🚀 : tolluset.ts:61: tc2=", tc2);

const tc3 = trie.startsWith("app"); // return True
console.info("🚀 : tolluset.ts:63: tc3=", tc3);

trie.insert("app");

const tc4 = trie.search("app"); // return True
console.info("🚀 : tolluset.ts:66: tc4=", tc4);
