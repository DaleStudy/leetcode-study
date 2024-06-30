# Complexity
- Time complexity: $$O(n)$$
    - 링크드 리스트의 길이 n에 대하여, 최악의 경우 모든 원소를 순회하므로 비용 `n`이 발생한다.

- Space complexity: $$O(n)$$
  - 링크드 리스트의 길이 n에 대하여, 최악의 경우 모든 원소를 순회하며 콜 스택에서 비용 `n`이 발생한다.
# Code
```go
func sizeOf(root *TreeNode) int {
	if root == nil {
		return 0
	}

	return sizeOf(root.Left) + sizeOf(root.Right) + 1
}

func kthSmallest(root *TreeNode, k int) int {
	leftSize := sizeOf(root.Left)
	if k < leftSize+1 {
		return kthSmallest(root.Left, k)
	} else if k == leftSize+1 {
		return root.Val
	} else {
		return kthSmallest(root.Right, k-leftSize-1)
	}
}

```