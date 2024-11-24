/*
풀이
- DFS
Big O
- N: 노드의 개수
- H: 트리의 높이
- Time complexity: O(N)
  - 모든 노드를 탐색합니다
- Space complexity: O(H)
  - 재귀호출 스택의 크기는 트리의 높이에 비례하여 증가합니다
*/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func maxDepth(root *TreeNode) int {
	maxDepth := 0
	var dig func(*TreeNode, int)
	dig = func(node *TreeNode, depth int) {
		if node == nil {
			if maxDepth < depth {
				maxDepth = depth
			}
			return
		}
		dig(node.Left, depth+1)
		dig(node.Right, depth+1)
	}
	dig(root, 0)
	return maxDepth
}

/*
풀이
- BFS
Big O
- N: 노드의 개수
- Time complexity: O(N)
  - 모든 노드를 탐색합니다
- Space complexity: O(N)
  - 노드 N개 짜리 트리에서 한 층의 폭은 N을 넘지 않습니다
    따라서 queue의 공간복잡도는 O(N)입니다
*/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxDepth(root *TreeNode) int {
	level := 0
	queue := make([]*TreeNode, 0)
	if root != nil {
		queue = append(queue, root)
		level++
	}
	for len(queue) > 0 {
		currQSize := len(queue)
		for currQSize > 0 {
			node := queue[0]
			queue = queue[1:]
			currQSize--
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		if len(queue) > 0 {
			level++
		}
	}
	return level
}
