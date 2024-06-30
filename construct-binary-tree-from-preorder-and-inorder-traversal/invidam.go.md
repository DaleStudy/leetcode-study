# Complexity
- Time complexity: $O(n)$
  - 원소의 크기 n에 대하여, 캐시 선언과 최악의 경우 순회에 비용 `n`이 발생한다.

- Space complexity: $O(n)$
  - 원소의 크기 n에 대하여, 캐시 선언과 최악의 경우 순회(콜 스택)에 비용 `n`이 발생한다.
# Code
```go
func buildTree(preorder []int, inorder []int) *TreeNode {
	cache := make(map[int]int)

	find := func(arr []int, val int) int {
		if len(cache) == 0 {
			cache = make(map[int]int, len(arr))
			for i, v := range arr {
				cache[v] = i
			}
		}
		return cache[val]
	}
	var organize func(preorder []int, inorder []int) *TreeNode
	organize = func(preorder []int, inorder []int) *TreeNode {
		if len(preorder) == 0 {
			return nil
		}
		rootIdx := find(inorder, preorder[0]) - find(inorder, inorder[0])

		return &TreeNode{
			Val:   preorder[0],
			Left:  organize(preorder[1:rootIdx+1], inorder[:rootIdx]),
			Right: organize(preorder[rootIdx+1:], inorder[rootIdx+1:]),
		}
	}

	return organize(preorder, inorder)
}

```