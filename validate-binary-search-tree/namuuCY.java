// 문제 풀이 흐름
// 기억하기로는 트리 순회 하는 방식이 몇 가지 있던거로 기억하는데
// 왼쪽 자식 -> 부모 -> 오른쪽 자식 이 방식으로 순회하는 방식을 사용해야함.
// 그렇게 순회하도록 한 뒤, 순서대로 확인하는데 숫자가 증가하지 않는다면 invalid
// 순회 아이디어 : 재귀를 이용 + 이전 노드 방문 값을 항상 저장
//  맨 처음 노드 방문 값은 -2^32 로 하자 -> 맨 왼쪽 노드는 항상 그 다음이 되도록
// param : 현재 노드
// 왼쪽 자식이 있다면? 왼쪽 노드 방문,
//          없으면 무시
// 현재 노드 값 valid한지
// 오른쪽 자식이 있다면? 오른쪽 노드 방문

// n = node 갯수라고 한다면
// 시간복잡도 : O(n)
// 공간복잡도 : O(1)



/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

	long currentValue = -(1L << 33);

	public boolean isValidBST(TreeNode root) {
		return visitNode(root);
	}


	private boolean visitNode(TreeNode node) {
		// 왼쪽 자식
		if (node.left != null) {
			boolean isValid = visitNode(node.left);
			if (!isValid) return false;
		}

		// 현재 노드
		if (currentValue >= node.val) return false;
		currentValue = node.val;

		// 오른쪽 자식
		if (node.right != null) {
			boolean isValid = visitNode(node.right);
			if (!isValid) return false;
		}

		return true;
	}
}
