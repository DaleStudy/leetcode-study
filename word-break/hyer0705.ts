// using set
function wordBreak(s: string, wordDict: string[]): boolean {
  const sLen = s.length;

  const dp: boolean[] = new Array(sLen + 1).fill(false);
  dp[0] = true;

  const wordSet = new Set<string>(wordDict);

  for (let i = 1; i <= sLen; i++) {
    for (let j = 0; j < i; j++) {
      if (dp[j] && wordSet.has(s.substring(j, i))) {
        dp[i] = true;
        break;
      }
    }
  }

  return dp[sLen];
}

// using trie
class TNode {
  isEndOf: boolean;
  children: Map<string, TNode>;

  constructor() {
    this.isEndOf = false;
    this.children = new Map<string, TNode>();
  }
}

class Trie {
  root: TNode;

  constructor() {
    this.root = new TNode();
  }

  insert(word: string): void {
    let currentNode = this.root;

    for (const ch of word) {
      if (!currentNode.children.has(ch)) {
        currentNode.children.set(ch, new TNode());
      }

      currentNode = currentNode.children.get(ch)!;
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
}

function wordBreak(s: string, wordDict: string[]): boolean {
  const sLen = s.length;

  const dp: boolean[] = new Array(sLen + 1).fill(false);
  dp[0] = true;

  const trie = new Trie();

  for (const word of wordDict) {
    trie.insert(word);
  }

  for (let i = 1; i <= sLen; i++) {
    for (let j = 0; j < i; j++) {
      if (dp[j]) {
        if (trie.search(s.substring(j, i))) {
          dp[i] = true;
          break;
        }
      }
    }
  }

  return dp[sLen];
}
