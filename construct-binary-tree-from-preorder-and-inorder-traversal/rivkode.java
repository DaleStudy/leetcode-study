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

import java.util.*;

class Solution {
    private int preIdx = 0;
    private Map<Integer, Integer> inPos = new HashMap<>();

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // inorder 값의 위치를 미리 저장: value -> index
        for (int i = 0; i < inorder.length; i++) {
            inPos.put(inorder[i], i);
        }

        return build(preorder, 0, inorder.length - 1);
    }

    private TreeNode build(int[] preorder, int inLeft, int inRight) {
        // inorder 구간이 비면 서브트리 없음
        if (inLeft > inRight) return null;

        // preorder에서 현재 루트 꺼내기
        int rootVal = preorder[preIdx++];
        TreeNode root = new TreeNode(rootVal);

        // inorder에서 루트 위치 찾기
        int k = inPos.get(rootVal);

        // 왼쪽 서브트리: inorder[inLeft .. k-1]
        root.left = build(preorder, inLeft, k - 1);

        // 오른쪽 서브트리: inorder[k+1 .. inRight]
        root.right = build(preorder, k + 1, inRight);

        return root;
    }
}
