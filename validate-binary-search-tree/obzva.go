/*
풀이
- BST의 속성을 이해한 후, 해당 속성을 검사하는 dfs 함수를 이용하면 풀이할 수 있습니다
Big O
- N: root 트리의 노드 개수
- Time complexity: O(N)
  - 모든 노드에 대해 최대 1번의 탐색이 필요합니다
- Space complexity: O(logN) (O(N) at worst)
  - check 함수의 재귀호출 스택 깊이는 트리의 높이에 비례하여 증가하므로 일반적으로 O(logN)의 공간복잡도를 가진다고 볼 수 있습니다
    하지만 트리가 심하게 치우친 경우 O(N)까지 커질 수 있습니다
*/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

 const (
	MIN = -(2_147_483_648 + 1)
	MAX = 2_147_483_647 + 1
)

func isValidBST(root *TreeNode) bool {
	return check(root.Left, MIN, root.Val) && check(root.Right, root.Val, MAX)
}

/*
helper dfs function
*/

func check(node *TreeNode, min int, max int) bool {
	// base case
	if node == nil {
		return true
	}
	// node.val should be in the boundary (min, max)
	if !(min < node.Val && node.Val < max) {
		return false
	}
	// check for children nodes
	return check(node.Left, min, node.Val) && check(node.Right, node.Val, max)
}
