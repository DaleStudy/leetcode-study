/*
 * 아이디어
 * 삽입된 전체 word를 저장해둔다. =>  wordSet
 * 삽입된 단어의 1글자 ~ 단어길이 글자 만큼을 전부 각각 prefix로 저장해둔다. => prefixSet
 * 중복처리를 위해 Set을 사용한다.
 */
class Trie {
  wordSet: Set<string>;
  prefixSet: Set<string>;

  constructor() {
    this.wordSet = new Set();
    this.prefixSet = new Set();
  }

  // TC: O(n) // n = word.length
  // SC: O(n)
  insert(word: string): void {
    let result = "";
    for (let i = 0; i < word.length; i++) {
      result += word[i];
      this.prefixSet.add(result);
    }
    this.wordSet.add(word);
  }

  // TC: O(1)
  // SC: O(1)
  search(word: string): boolean {
    return this.wordSet.has(word);
  }

  // TC: O(1)
  // SC: O(1)
  startsWith(prefix: string): boolean {
    return this.prefixSet.has(prefix);
  }
}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
