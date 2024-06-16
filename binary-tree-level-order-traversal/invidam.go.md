# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
트리를 순회하는 방법들 중, 레벨 순서대로 순회하는 방식을 알고있어 이를 이용했다.
# Approach
1. BFS를 진행한다.
2. 진행하기 전, 해당 레벨에 몇개의 원소가 있는지(`currLen`)을 저장한다.
3. 저장된 원소만큼 순회했다면, 레벨을 다 둘러본 것이므로 부가작업(`levels = append(levels, level)`)을 한다.

# Complexity
- Time complexity: $O(n)$
  - 트리의 원소를 n개라고 했을 때, 모든 원소를 순회하는 비용 `O(n)`이 소모된다.
- Space complexity: $O(n)$
  - 트리의 원소를 n개라고 했을 때, 모든 원소들을 저장하는 배열이 `O(n)`을 소모한다.

# Code
```go
func levelOrder(root *TreeNode) [][]int {
	levels := make([][]int, 0)

	if root == nil {
		return levels
	}

	q := []*TreeNode{root}

	for len(q) > 0 {
		level := make([]int, 0)
		currLen := len(q)
		for i := 0; i < currLen; i++ {
			front := q[0]
			level = append(level, front.Val)
			q = q[1:]

			if front.Left != nil {
				q = append(q, front.Left)
			}
			if front.Right != nil {
				q = append(q, front.Right)
			}
		}
		levels = append(levels, level)
	}

	return levels
}

```

```go
func levelOrder(root *TreeNode) [][]int {
	levels := make([][]int, 0)

	if root == nil {
		return levels
	}

	q := []*TreeNode{root}
	var nextQ []*TreeNode

	for len(q) > 0 {
		level := make([]int, 0)
		for _, front := range q {
			level = append(level, front.Val)

			if front.Left != nil {
				nextQ = append(nextQ, front.Left)
			}
			if front.Right != nil {
				nextQ = append(nextQ, front.Right)
			}
		}
		q, nextQ = nextQ, q[:0]

		levels = append(levels, level)
	}

	return levels
}

```
- 첫 번째 코드는 `q[1:]`을 이용해서 큐의 `pop()`을 구현한다. 하지만 GoLang에서는 `pop()`을 한다고해서, 참조가 해제되지 않아 메모리를 계속 잡아먹는다.
  - `pop()`을 하더라도 `q`가 순회하는 모든 원소들을 참조하고 있다. 
- 두 번째 코드는 `q, nextQ = nextQ, q[:0]`을 이용해서 `q`와 `nextQ`의 메모리 영역을 교체할 뿐, 부가적인 메모리 공간을 필요로 하지 않아 더욱 효율적이다. 