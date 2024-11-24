/*
풀이
- 두 트리가 동일한지 검사하는 dfs 함수를 이용하여 풀이할 수 있습니다
Big O
- M: root 트리의 노드 개수
- N: subRoot 트리의 노드 개수
- Time complexity: O(MN)
  - 최악의 경우 root 트리의 모든 노드에 대해 isSameTree 함수를 실행 (O(M))
    최악의 경우 isSameTree 함수는 O(N)의 시간복잡도를 가짐
- Space complexity: O(M+N)
  - isSubTree의 재귀호출스택 깊이는 최대 O(M)의 공간복잡도를 가짐
  - isSameTree의 재귀호출스택 깊이는 최대 O(N)의 공간복잡도를 가짐
*/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func isSubtree(root *TreeNode, subRoot *TreeNode) bool {
	// handling nil(null) inputs
	if root == nil {
		return false
	}
	// return true if root and subroot are same
	if isSameTree(root, subRoot) {
		return true
	}
	// else, check root.left and root.right
	return isSubtree(root.Left, subRoot) || isSubtree(root.Right, subRoot)
}

/*
dfs helper function checking whether two treenodes are same or not
*/
func isSameTree(a *TreeNode, b *TreeNode) bool {
	// handling nil(null) cases
	if a == nil || b == nil {
		return a == b
	}
	// falsy cases
	if a.Val != b.Val || !isSameTree(a.Left, b.Left) || !isSameTree(a.Right, b.Right) {
		return false
	}
	// else, return true
	return true
}
