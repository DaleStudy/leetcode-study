func findWords(board [][]byte, words []string) []string {
	root := &TrieNode{}
	for _, w := range words {
		root.Insert(w)
	}

	m, n := len(board), len(board[0])
	results := []string{}

	var dfs func(r, c int, node *TrieNode)
	dfs = func(r, c int, node *TrieNode) {
		ch := board[r][c]
		if ch == '#' {
			return
		}
		idx := ch - 'a'
		next := node.children[idx]
		if next == nil {
			return
		}
		if next.word != "" {
			results = append(results, next.word)
			next.word = ""
		}

		board[r][c] = '#'
		for _, d := range directions {
			nr, nc := r+d[0], c+d[1]
			if nr >= 0 && nr < m && nc >= 0 && nc < n {
				dfs(nr, nc, next)
			}
		}
		board[r][c] = ch
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			dfs(i, j, root)
		}
	}

	return results
}

type TrieNode struct {
	children [26]*TrieNode
	word     string
}

func (t *TrieNode) Insert(word string) {
	node := t
	for _, ch := range word {
		idx := ch - 'a'
		if node.children[idx] == nil {
			node.children[idx] = &TrieNode{}
		}
		node = node.children[idx]
	}
	node.word = word
}

var directions = [][]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
