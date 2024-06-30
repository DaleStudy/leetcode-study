# Complexity
- Time Complexity: $O(V+E)$
  - 정점의 수 V와 간선의 수 E에 대해, 모든 정점의 수 만큼 재귀호출이 일어거나 모든 간선의 수 만큼 반복문이 실행되므로 `V+E` 이다.
- Space Complexity: $O(V+E)$
  - 정점의 수 V와 간선의 수 E에 대해, 모든 정점의 수 만큼 복제본들을 저장하는 배열(`copied`)가 선언되고 모든 간선의 수 만큼 배열(`Neighbors`)가 선언되므로 `V+E` 이다.

# Code
```go
func deepCopy(node *Node, copied map[int]*Node) *Node {
	if node == nil {
		return nil
	}
	copied[node.Val] = &Node{
		Val:       node.Val,
		Neighbors: make([]*Node, len(node.Neighbors)),
	}

	for i := 0; i < len(node.Neighbors); i++ {
		if c, found := copied[node.Neighbors[i].Val]; found {
			copied[node.Val].Neighbors[i] = c
			continue
		}
		copied[node.Val].Neighbors[i] = deepCopy(node.Neighbors[i], copied)
	}

	return copied[node.Val]
}

func cloneGraph(node *Node) *Node {
	return deepCopy(node, make(map[int]*Node, 0))
}

```