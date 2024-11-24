/*
풀이
- Trie 자료구조와 2차원 배열에서의 DFS & Backtracking을 사용하여 풀이할 수 있습니다
Big O
- M, N: 주어진 2차원 배열 board의 행, 열 크기
- Max(W): 주어진 배열 words 중에서 가장 길이가 긴 단어의 길이
- Sum(W): 주어진 배열 words에 포함된 모든 단어의 길이의 총합
- Time complexity: O(Sum(W) + MN * Max(W))
  - building trie: O(Sum(W))
    - 각 단어의 모든 문자를 한 번씩 조회합니다
  - 반복문: O(MN * Max(W))
    - 행, 열에 대한 반복: O(MN)
    - dfs: O(Max(W))
      - 한 좌표에 대해 dfs 함수를 trie의 최대 깊이, 즉 O(Max(W))만큼 호출합니다
- Space complexity: O(Sum(W) + Max(W))
    - building trie: O(Sum(W)) at worst
    - dfs: O(Max(W))
      - 재귀 호출 스택의 깊이를 고려해야 합니다
*/

func findWords(board [][]byte, words []string) []string {
	// building trie
	root := &trieNode{}
	for _, w := range words {
		root.add(w)
	}

	m := len(board)
	n := len(board[0])
	res := make([]string, 0, len(words)) // create result
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			if len(res) == len(words) { // early break if we found all the words
				break
			}
			if root.children[idx(board[r][c])] != nil { // dfs if you found starting letter of any words
				dfs(r, c, &board, root, &res)
			}
		}
	}

	return res
}

// ----- Implementation of TrieNode -----
type trieNode struct {
	children [26]*trieNode
	word     string
}

func (t *trieNode) add(w string) {
	for i, c := range w {
		if t.children[c-'a'] == nil { // create new child node if there wasn't
			t.children[c-'a'] = &trieNode{}
		}
		t = t.children[c-'a']
		if i == len(w)-1 {
			t.word = w
		}
	}
}

// ----- Dfs -----
func dfs(r, c int, board *[][]byte, parentNode *trieNode, res *[]string) {
	currLetter := (*board)[r][c]
	currNode := parentNode.children[idx(currLetter)]
	// if current trie node represents some word, then append it to the result
	if currNode.word != "" {
		*res = append(*res, currNode.word)
		currNode.word = "" // prevent duplicate words into the result
	}
	// mark current cell as visited
	(*board)[r][c] = '#'
	// search for the 4 directions
	m := len(*board)
	n := len((*board)[0])
	dr := []int{0, 0, 1, -1}
	dc := []int{1, -1, 0, 0}
	for i := 0; i < 4; i++ {
		nr := r + dr[i]
		nc := c + dc[i]
		if !(0 <= nr && nr < m) || !(0 <= nc && nc < n) { // skip the invalid coordinates
			continue
		}
		if (*board)[nr][nc] == '#' { // skip the visited cell
			continue
		}
		if currNode.children[idx((*board)[nr][nc])] != nil {
			dfs(nr, nc, board, currNode, res)
		}
	}
	// restore the cell
	(*board)[r][c] = currLetter
}

// ----- Helper -----
func idx(b byte) int {
	return int(b - 'a')
}
