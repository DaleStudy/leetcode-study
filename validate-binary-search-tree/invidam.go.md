# Intuition (Array)
BST는 정렬 관계를 만족하므로, 순서에 맞게 배열에 저장한 후 정렬 관계가 맞는지 비교했다.
# Approach
<!-- Describe your approach to solving the problem. -->
1. 중위 순회(좌 --> 루트 --> 우)를 하며 배열을 채운다. (`fillNodes()`)
2. 배열을 순회하며 정렬 관계가 벗어났는지 판별한다. (`if nodes[i] >= nodes[i+1]`)

# Complexity
- Time complexity: $O(n)$
  - 트리의 원소를 n개라고 했을 때, 모든 원소를 순회하는 비용 `O(n)`이 소모된다.
- Space complexity: $O(n)$
  - 트리의 원소를 n개라고 했을 때, 모든 원소들을 저장하는 배열이 `O(n)`을 소모한다.

# Code
```go
func fillNodes(root *TreeNode) []int {
	nodes := make([]int, 0)
	if root.Left != nil {
		nodes = append(nodes, fillNodes(root.Left)...)
	}
	nodes = append(nodes, root.Val)
	if root.Right != nil {
		nodes = append(nodes, fillNodes(root.Right)...)
	}
	return nodes
}

func isValidBST(root *TreeNode) bool {
	nodes := fillNodes(root)
	for i := 0; i < len(nodes)-1; i++ {
		if nodes[i] >= nodes[i+1] {
			return false
		}
	}
	return true
}

```
# Intuition (Recursion)
예제를 참고했을 때, BST의 범위(최소, 최대)를 벗어나지 않는지를 유지하면 판별할 수 있다고 생각했다.
# Approach
<!-- Describe your approach to solving the problem. -->
1. 전위 순회(루트 --> 좌 --> 우)를 한다.
2. 해당 노드에서 주어진 범위를 벗어나는지 판별한다. (`if !(min < root.Val && root.Val < max)`)
3. 자식 노드들에 대해서도 BST가 만족하는지 재귀함수 호출을 통해 판별한다.
  - 가능한 범위는 해당 루트 노드를 기준으로 갱신한다.
# Complexity
- Time complexity: $O(n)$
  - 트리의 원소를 n개라고 했을 때, 모든 원소를 순회하는 비용 `O(n)`이 소모된다.
- Space complexity: $O(n)$
  - 트리의 원소를 n개라고 했을 때, 트리의 높이만큼 콜 스택이 발생하여 복잡도가 소모된다.
  - 최악의 경우(`skewed tree`), 높이는 `n`개이므로  `O(n)`을 소모한다.
  - 최선의 경우(`perfect binary tree`), 높이는 `log(n)`개 이므로 `O(log(n))`을 소모한다.

# Code
```go
func isValidBSTFrom(root *TreeNode, min, max int) bool {
	if root == nil {
		return true
	}
	if !(min < root.Val && root.Val < max) {
		return false
	}
	return isValidBSTFrom(root.Left, min, root.Val) && isValidBSTFrom(root.Right, root.Val, max)
}

func isValidBST(root *TreeNode) bool {
	return isValidBSTFrom(root, math.MinInt, math.MaxInt)
}

```

# Learned
- `math` 라이브러리의 `MinInt`, `MaxInt` 사용법 
  - `MinInt`는 `-1 << 31`로 계산한다.
    - 왜 `-`을 쉬프트하는지 궁금해서 찾아봤다.
    - 비트 맨뒤가 1인 수들은 `<< 31`을 하면 모두 `MinInt`를 만들 수 있지만, `1 << 31`로 `MaxInt`와 대비되도록 `-1`을 선택한 것 같다. 다른 수들에 비해 좀 더 직관적이기도 하다.

- `...` operator (Three dots, Ellipsis)
  - unpacking을 하는 용도이다.
  - 사례
    - 함수 인자로 몇 개인지 알 수 없는 인자들이 들어올 때
    - 배열 초기화 시 길이를 몰라 컴파일러에게 맡기고 싶을 때
  - 참고: [링크](https://blog.advenoh.pe.kr/go/Go%EC%97%90%EC%84%9C-%EC%82%BC-%EB%8F%84%ED%8A%B8-dot-%EC%82%AC%EC%9A%A9%EB%B0%A9%EB%B2%95-Three-Dots-Usage/)