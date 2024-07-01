# Complexity
- Insert
  - Time complexity: $$O(n)$$
    - `word`의 길이 n에 대하여, 깊이 n까지 재귀호출을 반복하는 비용이 발생한다.
  - Space complexity: $$O(n)$$
    - `word`의 길이 n에 대하여, 깊이 n까지 트라이 구조를 만드는 비용이 발생한다.
- Search
  - Time complexity: $$O(n)$$
    - `word`의 길이 n에 대하여, 깊이 n까지 재귀호출을 반복하는 비용이 발생한다.
  - Space complexity: $$O(1)$$
    - 별도 비용이 발생하지 않는다.
# Code
```go
type Trie struct {
	Val        byte
	IsTerminal bool
	Nodes      []*Trie
}

func Constructor() Trie {
	return Trie{Nodes: make([]*Trie, 26)}
}

func (this *Trie) Insert(word string) {
	if len(word) == 0 {
		return
	}

	if this.Nodes[word[0]-'a'] == nil {
		newNode := Constructor()
		this.Nodes[word[0]-'a'] = &newNode
		this.Nodes[word[0]-'a'].Val = word[0]
	}
	this.Nodes[word[0]-'a'].Insert(word[1:])
}

func (this *Trie) Search(word string) bool {
	if len(word) == 0 {
		return this.IsTerminal
	}
	if this.Nodes[word[0]-'a'] == nil {
		return false
	}
	return this.Nodes[word[0]-'a'].Search(word[1:])
}

func (this *Trie) StartsWith(prefix string) bool {
	if len(prefix) == 0 {
		return true
	}
	if this.Nodes[prefix[0]-'a'] == nil {
		return false
	}
	return this.Nodes[prefix[0]-'a'].StartsWith(prefix[1:])
}

```