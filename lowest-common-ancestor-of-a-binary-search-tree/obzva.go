/*
풀이
- common ancestor라는 조건에 맞는 node를 찾아냅니다
  for common ancestor C, left subtree of C includes p (p.Val <= C.Val)
                     and right subtree of C includes q (C.Val <= q.Val)
  이러한 조건을 만족하는 common ancestor는 BST에 하나만 존재합니다
  따라서 common ancestor를 찾으면 그게 곧 lowest common ancestor입니다
Big O
- N: 노드의 개수
- H: 트리의 높이 (avg: logN, worst: N)
- Time complexity: O(H)
- Space complexity: O(H)
*/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val   int
 *     Left  *TreeNode
 *     Right *TreeNode
 * }
 */

 func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	if p.Val > q.Val { // p < q가 되도록 함
		return lowestCommonAncestor(root, q, p)
	}
	if p.Val <= root.Val && root.Val <= q.Val { // common ancestor를 찾음
		return root
	} else if q.Val < root.Val { // left subtree 탐색
		return lowestCommonAncestor(root.Left, p, q)
	} else { // right subtree 탐색
		return lowestCommonAncestor(root.Right, p, q)
	}
}
