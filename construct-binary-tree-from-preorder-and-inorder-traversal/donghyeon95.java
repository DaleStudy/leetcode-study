import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

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

class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;

	TreeNode() {
	}

	TreeNode(int val) {
		this.val = val;
	}

	TreeNode(int val, TreeNode left, TreeNode right) {
		this.val = val;
		this.left = left;
		this.right = right;
	}

	public void setVal(int val) {
		this.val = val;
	}

	public void setLeft(TreeNode left) {
		this.left = left;
	}

	public void setRight(TreeNode right) {
		this.right = right;
	}

	public int getVal() {
		return val;
	}

	public TreeNode getLeft() {
		return left;
	}

	public TreeNode getRight() {
		return right;
	}
}

class Solution {
	int[] preList;
	List<Integer> inList;
	HashMap<Integer, TreeNode> treeNodes = new HashMap<>();

	public TreeNode buildTree(int[] preorder, int[] inorder) {
		preList = preorder;
		inList = Arrays.asList(Arrays.stream(inorder).boxed().toArray(Integer[]::new));
		List<Integer> preL = Arrays.asList(Arrays.stream(preorder).boxed().toArray(Integer[]::new));

		int preIndex = 0;
		int rootVal = preorder[0];
		TreeNode root = new TreeNode(rootVal);
		treeNodes.put(rootVal, root);

		while (preIndex < preList.length - 1) {
			System.out.println(preIndex);
			int inIndex = inList.indexOf(preList[preIndex]);
			int inNextIndex = inList.indexOf(preList[preIndex + 1]);

			TreeNode node = new TreeNode(preList[preIndex + 1]);
			treeNodes.put(preList[preIndex + 1], node);

			if (inIndex > inNextIndex) {
				// 현재 node의 왼쪽 자식으로
				TreeNode nowNode = treeNodes.get(preList[preIndex]);
				nowNode.setLeft(node);
			} else {
				// inorder의 앞 중에서 가장 처음 inList에서 앞인게
				int value = 0;
				int ii = inNextIndex;
				while (ii >= 0) {
					value = inorder[ii - 1];
					int i = preL.indexOf(value);
					if (i < preIndex + 1) {
						treeNodes.get(preList[i]).setRight(node);
						break;
					}
					ii--;
				}

			}

			preIndex++;
		}

		return treeNodes.get(rootVal);
	}

}


