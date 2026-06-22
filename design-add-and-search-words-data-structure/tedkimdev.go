type WordDictionary struct {
	root *TrieNode
}

func Constructor() WordDictionary {
	return WordDictionary{root: NewTrieNode()}
}

// TC: O(n)
// SC: O(t + n)
// t = total number of TrieNodes created so far
func (this *WordDictionary) AddWord(word string) {
	cur := this.root
	for _, c := range word {
		if cur.Children[c-'a'] == nil {
			cur.Children[c-'a'] = NewTrieNode()
		}
		cur = cur.Children[c-'a']
	}
	cur.IsWord = true
}

// TC: O(n)
func (this *WordDictionary) Search(word string) bool {
	return this.dfs(word, 0, this.root)
}

func (this *WordDictionary) dfs(word string, index int, root *TrieNode) bool {
	cur := root
	for i := index; i < len(word); i++ {
		c := word[i]
		if c == '.' {
			for _, child := range cur.Children {
				if child != nil && this.dfs(word, i+1, child) {
					return true
				}
			}
			return false
		} else {
			if cur.Children[c-'a'] == nil {
				return false
			}
			cur = cur.Children[c-'a']
		}
	}
	return cur.IsWord
}

type TrieNode struct {
	Children [26]*TrieNode
	IsWord   bool
}

func NewTrieNode() *TrieNode {
	return &TrieNode{}
}
