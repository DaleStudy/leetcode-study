/**
 * @class - Dictionary 구현
 * @description
 * - .의 경우 모든 문자와 일치
 * - .일 경우 결국 모든 children 조회필요 => dfs
 */

class WordNode {
  children: { [key: string]: WordNode };
  endOfWord: boolean;
  constructor() {
    this.children = {};
    this.endOfWord = false;
  }
}

class WordDictionary {
  private rootNode: WordNode;
  constructor() {
    this.rootNode = new WordNode();
  }

  addWord(word: string): void {
    let nodeInstance = this.rootNode;

    for (const str of word) {
      if (!nodeInstance.children[str]) {
        nodeInstance.children[str] = new WordNode();
      }
      nodeInstance = nodeInstance.children[str];
    }

    nodeInstance.endOfWord = true;
  }

  search(word: string): boolean {
    return this.searchDfs(this.rootNode, word, 0);
  }

  private searchDfs(currentNode: WordNode, word: string, idx: number): boolean {
    if (idx === word.length) {
      return currentNode.endOfWord;
    }

    const char = word[idx];
    if (char === ".") {
      for (const key in currentNode.children) {
        const childSearch = this.searchDfs(
          currentNode.children[key],
          word,
          idx + 1
        );
        if (childSearch) {
          return true;
        }
      }

      return false;
    } else {
      if (!currentNode.children[char]) {
        return false;
      }

      return this.searchDfs(currentNode.children[char], word, idx + 1);
    }
  }
}

const wordDict = new WordDictionary();

wordDict.addWord("at");
wordDict.addWord("and");
wordDict.addWord("an");
wordDict.addWord("add");

wordDict.search("a"); // false
wordDict.search(".at"); // false

wordDict.addWord("bat");

wordDict.search(".at"); // true
wordDict.search("an."); // true
wordDict.search("a.d."); // false
wordDict.search("b."); // false
wordDict.search("a.d"); // true
wordDict.search("."); // false



