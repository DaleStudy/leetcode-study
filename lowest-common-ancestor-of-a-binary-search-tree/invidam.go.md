# Intuition
이전에 풀어봤던 문제였다! 어려운 문제였다는 생각을 벗어던지고 최대한 간단하게 풀어보려고 했다.
# Approach
<!-- Describe your approach to solving the problem. -->
1. 두 노드(`p`, `q`) 모두 어떠한 경로를 거쳐, 해당 노드까지 도착하는지 조상들을 배열(`routes`)에 저장한다.
2. 배열을 하나씩 비교해가며, 두 노드가 엇갈리는 지점(`pRoutes[idx] != qRoutes[idx]`)을 찾는다.
3. 그 지점 바로 이전 지점(`[idx-1]`)이 최소 공통 조상이다.
# Complexity
- Time complexity
  - 평균: $O(log(n))$
  - 최악: $O(n)$
  - 트리의 높이만큼 순회를 하게된다. 노드가 n개 이므로, 트리의 높이는 최선 `log(n)`, 최악 `n`이 된다.

- Space complexity
    - 평균: $O(log(n))$
    - 최악: $O(n)$
    - 트리의 높이만큼 순회를 하게된다. 노드가 n개 이므로, 트리의 높이는 최선 `log(n)`, 최악 `n`이 된다.

# Code
```go
func getRoutes(head, target *TreeNode) []*TreeNode {
	routes := make([]*TreeNode, 0)

	curr := head
	for curr.Val != target.Val {
		routes = append(routes, curr)
		if target.Val == curr.Val {
			break
		} else if target.Val < curr.Val {
			curr = curr.Left
		} else {
			curr = curr.Right
		}
	}
	return append(routes, curr)
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	pRoutes := getRoutes(root, p)
	qRoutes := getRoutes(root, q)

	idx := 0
	for idx < min(len(pRoutes), len(qRoutes)) && pRoutes[idx] == qRoutes[idx] {
		idx++
	}

	return pRoutes[idx-1]
}

```
# Intuition & Approach
(솔루션의 해결법 참고)

두 노드는 공통조상까지는 동일한 대소관계를 가지고 있다가, 공통 조상 이후로 대소관계가 구분된다.
따라서, 루트에서 동일한 대소관계가 있는 조상까지 이동한다. (다시 말해, 대소 관계가 구분되는 특정 지점이 발생한다면 그 지점의 부모가 공통 조상이다.)
# Complexity
- Time complexity
  - 평균: $O(log(n))$
  - 최악: $O(n)$
  - 트리의 높이만큼 순회를 하게된다. 노드가 n개 이므로, 트리의 높이는 최선 `log(n)`, 최악 `n`이 된다.

- Space complexity: $O(1)$
  - 별도 자료구조를 사용하지 않고, 링크드 리스트의 순회만이 존재한다.

# Code
## For-loop
```go
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	curr := root
	for {
		if p.Val < curr.Val && q.Val < curr.Val {
			curr = curr.Left
		} else if p.Val > curr.Val && q.Val > curr.Val {
			curr = curr.Right
		} else {
			break
		}
	}
	return curr
}

```
## Recursion
```go
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	if p.Val < root.Val && q.Val < root.Val {
		return lowestCommonAncestor(root.Left, p, q)
	} else if p.Val > root.Val && q.Val > root.Val {
		return lowestCommonAncestor(root.Right, p, q)
	}
	return root
}

```
: 함수 콜스택이 트리의 높이만큼 증가하므로, 공간 복잡도가 O(n)까지 증가할 수 있다. (처음 해결법의 공간 복잡도처럼.) 