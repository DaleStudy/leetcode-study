// TC: O(n)
// SC: O(t) - Where n is the length of the string and t is the total number of TrieNodes created in the Trie.
type PrefixTree struct {
	children map[rune]*PrefixTree
	isWord   bool
}

func Constructor() PrefixTree {
	return PrefixTree{
		children: map[rune]*PrefixTree{},
		isWord:   false,
	}
}

func (this *PrefixTree) Insert(word string) {
	cur := this
	for _, c := range word {
		if _, ok := cur.children[c]; !ok {
			child := Constructor()
			cur.children[c] = &child
			cur = cur.children[c]
		} else {
			cur = cur.children[c]
		}
	}
	cur.isWord = true
}

func (this *PrefixTree) Search(word string) bool {
	cur := this
	for _, c := range word {
		if _, ok := cur.children[c]; ok {
			cur = cur.children[c]
		} else {
			return false
		}
	}
	return cur.isWord
}

func (this *PrefixTree) StartsWith(prefix string) bool {
	cur := this
	for _, c := range prefix {
		if _, ok := cur.children[c]; ok {
			cur = cur.children[c]
		} else {
			return false
		}
	}

	return cur != nil
}
