/**
test case 를 분석해본 결과, 결국 문자열에 대한 트리를 구성해야 하는 것으로 보임
트리는 노드로 구성할 수 있을 듯 하지만, 구현하지 않고 hash 의 연속을 만들어보는 것으로 하자.

오래걸렸지만 한번에 성공! 시간 복잡도: O(n), 공간 복잡도: O(1) 정도인 듯
 */
class Trie {
  constructor(private letterHash: any = {}) {}

  insert(word: string): void {
    let currentHash = this.letterHash;

    for (let i = 0; i < word.length; i++) {
      const existHash = currentHash[word[i]];
      if (existHash) {
        currentHash = existHash;
      } else {
        currentHash[word[i]] = {};
        currentHash = currentHash[word[i]];
      }
    }

    currentHash["count"] = currentHash["count"] ? currentHash["count"] + 1 : 1;
  }

  search(word: string): boolean {
    let currentHash = this.letterHash;

    for (let i = 0; i < word.length; i++) {
      const existHash = currentHash[word[i]];
      // console.log(`search ${word}`, JSON.stringify(existHash), word[i])
      if (existHash) {
        currentHash = existHash;
      } else {
        return false;
      }
    }

    return !!currentHash["count"];
  }

  startsWith(prefix: string): boolean {
    let currentHash = this.letterHash;

    for (let i = 0; i < prefix.length; i++) {
      const existHash = currentHash[prefix[i]];
      // console.log(`startsWith ${prefix}`, JSON.stringify(existHash), prefix[i])
      if (existHash) {
        currentHash = existHash;
      } else {
        return false;
      }
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
