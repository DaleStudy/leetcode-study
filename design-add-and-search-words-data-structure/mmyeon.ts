/**
 *@link https://leetcode.com/problems/design-add-and-search-words-data-structure/
 *
 * 접근 방법 :
 *  - set 활용하는 방법
 * - 단어 추가할 때는 set에 저장하고, 단어 찾을 때마다 cache목록에서 값 가져오기.
 * - 단어 추가하면 이전 캐시는 사용하지 못하니까 클리어 해주기
 * - 이전 값 활용한다는 장점이 있지만 단어  추가시 다시 캐시 만들어야하는 비효율 존재
 *
 * 시간복잡도 : O(n * k)
 *  - n은 set에 추가된 단어 길이, k는 각 단어 평균 길이
 *  - this.set 단어 순회 => O(n)
 *  - replaceAll, filter =>  O(k)
 *
 * 공간복잡도 : O(n * k)
 * - n은 패턴의 개수, k는 패턴에 매칭되는 평균 단어 수
 */
class WordDictionary {
  set: Set<string>;
  cache: Map<string, string[]>;
  constructor() {
    this.set = new Set();
    this.cache = new Map();
  }

  addWord(word: string): void {
    this.set.add(word);
    // 새로운 단어가 추가 시 캐시 클리어
    this.cache.clear();
  }

  search(word: string): boolean {
    // 캐시에 값이 존재하면 즉시 리턴
    if (this.cache.has(word)) return this.cache.get(word)!.length > 0;

    // 정규표현식 패턴 생성
    const pattern = new RegExp(`^${word.replaceAll(".", "[a-z]")}$`);
    const matches = [...this.set].filter((item) => pattern.test(item));

    // 검색 결과 캐시에 저장
    this.cache.set(word, matches);

    return matches.length > 0;
  }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */

// 시간 복잡도 개선하기 위해서 Trie 자료 구조 사용
class TrieNode {
  children: Map<string, TrieNode>;
  isEndOfWord: boolean;

  constructor() {
    this.children = new Map();
    this.isEndOfWord = false;
  }
}

/*
 * 접근 방법 :
 *  - 각 문자 저장하고 검색하기 위해서 Trie 구조 사용
 *  - 와일드카드(.)가 포함된 단어는 모든 자식 노드 탐색하기 위해서 재귀적으로 확인
 *
 * 시간복잡도 : O(n * k)
 *  - n : 단어 개수, m : 단어 평균 길이 => addWord의 복잡도 :  O(n * m)
 *  - c : 자식노드 개수, d : 와일드카드 개수, m : 단어 길이  =>  search의 복잡도 :  O(c^d * m)
 *  - 와일드 카드 있는 경우 각 노드 별 모든 자식 노드를 탐색해야 한다.
 *
 * 공간복잡도 : O(n * k)
 *  - n은 패턴의 개수, k는 패턴에 매칭되는 평균 단어 수
 */
class WordDictionary {
  root: TrieNode;
  constructor() {
    this.root = new TrieNode();
  }

  addWord(word: string): void {
    let currentNode = this.root;

    for (const letter of word) {
      if (!currentNode.children.has(letter))
        currentNode.children.set(letter, new TrieNode());
      currentNode = currentNode.children.get(letter)!;
    }

    currentNode.isEndOfWord = true;
  }

  search(word: string): boolean {
    const dfs = (currentNode: TrieNode, index: number): boolean => {
      if (index === word.length) return currentNode.isEndOfWord;

      const char = word[index];
      // 와일드 카드인 경우 모든 자식 노드 순회한다
      if (char === ".") {
        // 모든 자식 노드 순회
        for (const key of currentNode.children.keys()) {
          if (dfs(currentNode.children.get(key)!, index + 1)) return true;
        }
        return false;
      } else {
        if (!currentNode.children.has(char)) return false;
        return dfs(currentNode.children.get(char)!, index + 1);
      }
    };

    return dfs(this.root, 0);
  }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
