// 시간복잡도
// addWord: O(n) (n은 추가하는 단어의 길이)
// search: O(m^n) (m은 각 노드의 최대 자식 수, n은 검색하는 단어의 길이)

// 공간복잡도
// addWord: O(n) (n은 추가하는 단어의 길이)
// search: O(n) (n은 검색하는 단어의 길이, 재귀 호출 스택의 깊이)

class TrieNode {
    constructor() {
        this.children = {}
        this.endOfWord = false
    }
}

class WordDictionary {
    constructor() {
        this.root = new TrieNode()
    }
    addWord(word) {
        let curNode = this.root

        for (let i = 0 ; i < word.length; i++) {
            if (!curNode.children[word[i]]) {
                curNode.children[word[i]] = new TrieNode();
            }

            curNode = curNode.children[word[i]];
        }

        curNode.endOfWord = true
    }
    search(word) {
        return this.searchInNode(word, this.root);
    }

    searchInNode(word, node) {
        let curNode = node;

        for (let i = 0; i < word.length; i++) {
            if (word[i] === '.') {
                for (let key in curNode.children) {
                    if (this.searchInNode(word.slice(i + 1), curNode.children[key])) return true
                }
                return false
            }

            if (word[i] !== '.') {
                if (!curNode.children[word[i]]) return false
                curNode = curNode.children[word[i]];
            }
        }

        return curNode.endOfWord
    }
}


const wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
console.log(wordDictionary.search("pad")); // return False
console.log(wordDictionary.search("bad")); // return True
console.log(wordDictionary.search(".ad")); // return True
console.log(wordDictionary.search("b..")); // return True


