import java.util.LinkedList;
import java.util.Queue;

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
	public boolean isSameTree(TreeNode p, TreeNode q) {
		// 트리 순회를 한다
		// 현재 순회한 값이 다르다면 return false
		if (p==null && q==null) return true;
		if (p==null && q!=null) return false;
		if (p!=null && q==null) return false;

		Queue<TreeNode> pQue = new LinkedList<>();
		pQue.add(p);
		Queue<TreeNode> qQue = new LinkedList<>();
		qQue.add(q);

		while (!pQue.isEmpty() && !qQue.isEmpty()) {
			TreeNode pNode = pQue.poll();
			TreeNode qNode = qQue.poll();

			if (pNode.val != qNode.val) return false;
			if (pNode.left!=null && qNode.left!=null) {
				pQue.add(pNode.left);
				qQue.add(qNode.left);
			} else if (pNode.left==null && qNode.left!=null) {
				return false;
			} else if (pNode.left!=null && qNode.left==null) {
				return false;
			}

			if (pNode.right!=null && qNode.right!=null) {
				pQue.add(pNode.right);
				qQue.add(qNode.right);
			} else if (pNode.right==null && qNode.right!=null) {
				return false;
			} else if (pNode.right!=null && qNode.right==null) {
				return false;
			}
		}

		return pQue.isEmpty() && qQue.isEmpty();

	}
}

