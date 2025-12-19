type ChildTrie = {
  value?: string;
  isEnd?: boolean;
  childrens: ChildrenMap;
};
type ChildrenMap = {
  [key: string]: ChildTrie;
};

class Trie {
  childrens: ChildrenMap = {};
  constructor() {}

  insert(word: string): void {
    if (word.length === 0) {
      return;
    }
    let current: ChildTrie = {
      childrens: this.childrens,
    };
    for (let i = 0; i < word.length; i++) {
      if (current.childrens[word[i]] === undefined) {
        current.childrens[word[i]] = { value: word[i], isEnd: false, childrens: {} };
      }

      current = current.childrens[word[i]];
    }
    current.isEnd = true;
  }

  search(word: string): boolean {
    let current: ChildTrie = {
      childrens: this.childrens,
    };
    for (let i = 0; i < word.length; i++) {
      if (current.childrens[word[i]] === undefined) {
        return false;
      }

      current = current.childrens[word[i]];
    }
    return current.isEnd ?? false;
  }

  startsWith(prefix: string): boolean {
    let current = this.childrens;
    for (let i = 0; i < prefix.length; i++) {
      if (current[prefix[i]] === undefined) {
        return false;
      }
      current = current[prefix[i]].childrens;
    }
    return true;
  }
}
