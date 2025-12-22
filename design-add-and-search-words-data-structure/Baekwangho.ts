/**
search 의 역할을 보았을 때, 각 글자의 길이별로 set 을 두는 형태로 구현해볼 수 있을 듯 하다.
class WordDictionary {
    setArray: Array<Set<string>>
    wordSet: Set<string>
    constructor() {
        this.setArray = Array.from({length:25}, () => new Set())
        this.wordSet = new Set()
    }

    addWord(word: string): void {
        for(let i=0; i<word.length; i++) {
            this.setArray[i].add(word[i])
        }
        this.wordSet.add(word)
    }

    search(word: string): boolean {
        if (word.includes('.')) {
            for(let i=0; i<word.length; i++) {
                console.log(word[i], this.setArray[i])
                if (word[i] === '.') {
                    if (this.setArray[i].size) continue
                    return false
                } else {
                    if (this.setArray[i].has(word[i])) continue
                    return false
                }
            }
            return true
        } else {
            if (this.wordSet.has(word)) return true
            return false
        }
    }
}
 */

/**
실패했다. 한글자의 '.' 케이스를 충족시킬 수 없었다. 
실제 word 기반한 데이터가 아니기 때문에 발생하는 오류인 듯 하다.
힌트에서 trie 를 얘기하니, 그것을 구현해보자.
...
근데 결국 search 에서 탐색이 최악의 경우 '..............n' 등에서 최악일 듯 하다.
...
하지만 힌트를 보니, dfs 기반으로 구현하라고 하는구나.

시간 복잡도: O(L) ~ O(n * L) / 공간 복잡도: O(n * L)
O(L) 은 search 에 wildcard 가 없을 때, L은 글자 길이
 */
class WordDictionary {
  headMap: any;

  constructor() {
    this.headMap = {};
  }

  addWord(word: string): void {
    let curMap = this.headMap;

    for (let i = 0; i < word.length; i++) {
      const cur = curMap[word[i]];
      if (!cur) {
        const temp = {};
        curMap[word[i]] = temp;
        curMap = temp;
      } else {
        curMap = cur;
      }
    }
    curMap["count"] ? curMap["count"]++ : (curMap["count"] = 1);
  }

  search(word: string): boolean {
    function call(dict: any, subset?: string): boolean {
      if (dict["count"] && !subset) {
        return true;
      }

      const firstChar = subset![0];
      if (firstChar === ".") {
        return Object.values(dict).some((el) =>
          call(el, subset!.slice(1, subset!.length))
        );
      } else {
        const firstCharDict = dict[firstChar];
        if (!firstCharDict) return false;

        return call(firstCharDict, subset!.slice(1, subset!.length));
      }
    }

    return call(this.headMap, word);
  }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
