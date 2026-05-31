// TC: O((n * t) + (m * t))
// SC: O(n + (m * t))
func wordBreak(s string, wordDict []string) bool {
	trie := NewTrieNode()
	maxLength := 0
	for _, word := range wordDict {
		trie.Insert(word)
		if len(word) > maxLength {
			maxLength = len(word)
		}
	}

	dp := make([]bool, len(s)+1)
	dp[len(s)] = true

	for i := len(s) - 1; i >= 0; i-- {
		node := trie
		for j := i; j < len(s) && j < i+maxLength; j++ {
			c := s[j]
			if _, ok := node.children[rune(c)]; !ok {
				break
			}
			node = node.children[rune(c)]

			if node.isWord && dp[j+1] {
				dp[i] = true
				break
			}
		}
	}

	return dp[0]
}

type TrieNode struct {
	children map[rune]*TrieNode
	isWord   bool
}

func NewTrieNode() *TrieNode {
	return &TrieNode{children: make(map[rune]*TrieNode)}
}

func (t *TrieNode) Insert(word string) {
	node := t
	for _, char := range word {
		if _, ok := node.children[char]; !ok {
			node.children[char] = NewTrieNode()
		}
		node = node.children[char]
	}
	node.isWord = true
}

// func (t *TrieNode) Search(s string, i, j int) bool {
//     node := t
//     for idx := i; idx <= j; idx++ {
//         char := rune(s[idx])
//         if _, ok := node.children[char]; !ok {
//             return false
//         }
//         node = node.children[char]
//     }
//     return node.isWord
// }


