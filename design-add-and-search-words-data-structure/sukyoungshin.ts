// 1번풀이 O(n × m)
class WordDictionary1 {
  private words: string[];
  constructor() {
    this.words = [];
  }

  addWord(word: string): void {
    this.words.push(word);
  }
  search(word: string): boolean {
    return this.words
      .filter((savedWord) => savedWord.length === word.length)
      .some((savedWord) => {
        for (let i = 0; i < word.length; i++) {
          if (word[i] === ".") continue;
          if (word[i] !== savedWord[i]) return false;
        }
        return true;
      });
  }
};

// 2번풀이 : Trie(트라이) 자료구조
type TrieNode = {
  children: { [key: string]: TrieNode };
  isEnd: boolean;
};

class WordDictionary {
  private root: TrieNode;
  constructor() {
    this.root = {
      children: {},
      isEnd: false,
    };
  }
  addWord(word: string): void {
    let node = this.root;

    for (let i = 0; i < word.length; i++) {
      const char = word[i];

      if (!node.children[char]) {
        node.children[char] = {
          children: {},
          isEnd: false,
        };
      }

      node = node.children[char];
    }

    node.isEnd = true;
  }
  search(word: string): boolean {
    const dfs = (node: TrieNode, index: number): boolean => {
      if (index === word.length) return node.isEnd;

      const char = word[index];

      if (char === ".") {
        for (const nextChar in node.children) {
          if (dfs(node.children[nextChar], index + 1)) {
            return true;
          }
        }
        return false;
      }

      if (!node.children[char]) return false;
      return dfs(node.children[char], index + 1);
    };

    return dfs(this.root, 0);
  }
};
