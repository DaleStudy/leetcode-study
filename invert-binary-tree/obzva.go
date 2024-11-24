/*
풀이 1
- 함수의 재귀호출을 이용해서 풀이할 수 있습니다

Big O
- N: 노드의 개수
- H: 트리의 높이
- Time complexity: O(N)
- Space complexity: O(H) (logN <= H <= N)
  - 재귀 호출 스택의 최대 깊이는 트리의 높이에 비례하여 증가합니다
*/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func invertTree(root *TreeNode) *TreeNode {
	if root == nil {
		return root
	}

	tmp := invertTree(root.Right)
	root.Right = invertTree(root.Left)
	root.Left = tmp

	return root
}

/*
풀이 2
- 큐와 반복문을 이용하여 풀이할 수 있습니다

Big O
- N: 노드의 개수
- Time complexity: O(N)
- Space complexity: O(N)
  - 큐의 최대 크기는 N / 2 를 넘지 않습니다
    큐의 최대 크기는 트리의 모든 층 중에서 가장 폭이 큰 층의 노드 수와 같습니다
	높이가 H인 트리의 최대 폭은 1. balanced tree일 때 2. 맨 아랫 층의 폭이고 이 때의 폭 W는 2^(H-1) 입니다
	높이가 H인 balanced tree의 노드 개수는 2^H - 1 = N 이므로 아래 관계가 성립합니다
	N/2 = (2^H - 1) / 2 = 2^(H-1) - 1/2 >= 2^(H-1) = W
	따라서 공간 복잡도는 O(N/2) = O(N) 입니다
*/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func invertTree(root *TreeNode) *TreeNode {
	queue := make([]*TreeNode, 0)
	queue = append(queue, root)

	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]

		if node == nil {
			continue
		}

		tmp := node.Left
		node.Left = node.Right
		node.Right = tmp

		queue = append(queue, node.Left, node.Right)
	}

	return root
}
