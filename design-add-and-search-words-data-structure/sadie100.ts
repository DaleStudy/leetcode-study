/*
words를 맵형태로 저장, 각 스펠링과 다음에 나오는 문자열을 key-value로 하는 맵으로 저장
.의 경우 모든 경우를 탐색한다

시간복잡도 :
    addWord : O(L) (L은 words의 길이)
    search : 일반적으로 O(L), .이 많으면 O(26^k) (k는 .의 개수)

*/
class TrieNode {
  children: Map<string, TrieNode>
  isEnd: boolean

  constructor() {
    this.children = new Map()
    this.isEnd = false
  }
}

class WordDictionary {
  words = new TrieNode()
  constructor() {}

  addWord(word: string): void {
    let curWords = this.words

    for (let i = 0; i < word.length; i++) {
      const char = word[i]

      if (!curWords.children.has(char)) {
        curWords.children.set(char, new TrieNode())
      }

      curWords = curWords.children.get(char)
    }
    curWords.isEnd = true
  }

  search(word: string): boolean {
    return this.searchRecursively(word, this.words)
  }

  searchRecursively(word: string, area: TrieNode) {
    for (let i = 0; i < word.length; i++) {
      if (!area) return false
      const char = word[i]

      if (char === '.') {
        const values = [...area.children.values()]

        for (let newArea of values) {
          const result = this.searchRecursively(word.slice(i + 1), newArea)
          if (result) return true
        }
        return false
      } else {
        if (!area.children.has(char)) return false
        area = area.children.get(char)
      }
    }

    if (area.isEnd) return true
    return false
  }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
