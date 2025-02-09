// 시간복잡도: O(n)
// 공간복잡도: O(n)

package main

type Trie struct {
	children map[byte]*Trie
	isEnd    bool
}

func Constructor() Trie {
	return Trie{children: make(map[byte]*Trie)}
}

func (this *Trie) Insert(word string) {
	for i := 0; i < len(word); i++ {
		if _, ok := this.children[word[i]]; !ok {
			this.children[word[i]] = &Trie{children: make(map[byte]*Trie)}
		}
		this = this.children[word[i]]
	}
	this.isEnd = true
}

func (this *Trie) Search(word string) bool {
	for i := 0; i < len(word); i++ {
		if _, ok := this.children[word[i]]; !ok {
			return false
		}
		this = this.children[word[i]]
	}
	if this.isEnd {
		return true
	}
	return false
}

func (this *Trie) StartsWith(prefix string) bool {
	for i := 0; i < len(prefix); i++ {
		if _, ok := this.children[prefix[i]]; !ok {
			return false
		}
		this = this.children[prefix[i]]
	}
	return true
}

/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */
