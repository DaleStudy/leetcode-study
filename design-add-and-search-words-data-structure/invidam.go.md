# Complexity
- AddWord
  - Time Complexity: $O(n)$
    - 단어의 길이 n만큼 재귀호출이 일어난다.
  - Space Complexity: $O(n)$
    - 단어의 길이 n만큼 재귀호출이 일어난다.
- Search
  - Time Complexity: $O(n)$
    - 단어의 길이 n만큼 재귀호출이 일어난다.
  - Space Complexity: $O(n)$
    - 단어의 길이 n만큼 재귀호출이 일어난다.
  - `.`의 개수, 단어의 범위는 모두 2, 26개로 상수개라 제외했다.


# Code

```go
type WordDictionary struct {
	Nodes        []*WordDictionary
	IsTerminated bool
}

func Constructor() WordDictionary {
	return WordDictionary{Nodes: make([]*WordDictionary, 26)}
}

func (this *WordDictionary) AddWord(word string) {
	if len(word) == 0 {
		this.IsTerminated = true
		return
	}

	if this.Nodes[word[0]-'a'] == nil {
		newNode := Constructor()
		this.Nodes[word[0]-'a'] = &newNode

	}
	this.Nodes[word[0]-'a'].AddWord(word[1:])
}

func (this *WordDictionary) Search(word string) bool {
	if len(word) == 0 {
		return this.IsTerminated
	}

	if word[0] == '.' {
		for c := 'a'; c <= 'z'; c++ {
			if this.Search(string(c) + word[1:]) {
				return true
			}
		}
		return false
	}

	if this.Nodes[word[0]-'a'] == nil {
		return false
	}
	return this.Nodes[word[0]-'a'].Search(word[1:])
}

```