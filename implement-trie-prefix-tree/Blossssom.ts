// 단순 구현 시 효율이 낮게 나옴
// class Trie {
//   private word: Set<string>;
//   constructor() {
//     this.word = new Set();
//   }

//   insert(word: string): void {
//     this.word.add(word);
//   }

//   search(word: string): boolean {
//     return this.word.has(word);
//   }

//   startsWith(prefix: string): boolean {
//     for (const str of this.word) {
//       if (prefix.length > str.length) {
//         continue;
//       }
//       let check = true;
//       for (let i = 0; i < prefix.length; i++) {
//         if (str[i] !== prefix[i]) {
//           check = false;
//           break;
//         }
//       }
//       if (check) {
//         return true;
//       }
//     }
//     return false;
//   }
// }

// 노드 구조를 개선
class TrieNode {
  children: { [key: string]: TrieNode };
  isEndOfWord: boolean;
  constructor() {
    this.children = {};
    this.isEndOfWord = false;
  }
}

class Trie {
  private root: TrieNode;
  constructor() {
    this.root = new TrieNode();
  }

  insert(word: string): void {
    // 글자 하나씩 TrieNode 타입으로 저장
    let currentNode = this.root;
    for (const char of word) {
      if (!currentNode.children[char]) {
        currentNode.children[char] = new TrieNode();
      }

      currentNode = currentNode.children[char];
    }
    currentNode.isEndOfWord = true;
    console.log(this.root);
  }

  // 각 글자를 TrieNode에서 서칭하며 판단
  search(word: string): boolean {
    let currentNode = this.root;
    for (const char of word) {
      if (!currentNode.children[char]) {
        return false;
      }
      currentNode = currentNode.children[char];
    }
    return currentNode.isEndOfWord;
  }

  // 동일 로직이지만 prefix 만큼만 존재하면 true
  startsWith(prefix: string): boolean {
    let currentNode = this.root;
    for (const char of prefix) {
      if (!currentNode.children[char]) {
        return false;
      }
      currentNode = currentNode.children[char];
    }
    return true;
  }
}

const trie = new Trie();
trie.insert("apple");
trie.search("apple"); // true
trie.search("app"); // false
trie.startsWith("app"); // true
trie.insert("app");
trie.search("app"); // true


