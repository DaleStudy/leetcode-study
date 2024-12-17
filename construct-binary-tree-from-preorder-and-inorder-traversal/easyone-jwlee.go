// 풀이
// preorder[0]이 제일 꼭대기
// preorder 배열의 root index, inorder 배열의 시작, inorder 배열의 끝
// 위의 세가지를 parameter로 받는 재귀함수를 만들어서
// 왼쪽 서브트리, 오른쪽 서브트리를 순회

// TC
// map 만들기 O(n) + 재귀함수는 각 노드를 딱 한번씩만 방문하므로 O(n) = O(n)

// SC
// map O(n) + 재귀함수 최악의 경우 한쪽으로만 노드가 이어지는 경우 O(n) = O(n)

func buildTree(preorder []int, inorder []int) *TreeNode {
	inorderMap := make(map[int]int)
	for i, n := range inorder {
		inorderMap[n] = i
	}

	var recursive func(rootIndex, inStart, inEnd int) *TreeNode
	recursive = func(rootIndex, inStart, inEnd int) *TreeNode {
		if rootIndex >= len(preorder) || inStart > inEnd {
			return nil
		}
		rootVal := preorder[rootIndex]
		rootInorderIndex := inorderMap[rootVal]

		result := &TreeNode{
			Val: rootVal,
		}

		leftSize := rootInorderIndex - inStart

		result.Left = recursive(rootIndex+1, inStart, rootInorderIndex-1)
		result.Right = recursive(rootIndex+1+leftSize, rootInorderIndex+1, inEnd)

		return result
	}

	return recursive(0, 0, len(inorder)-1)
}
