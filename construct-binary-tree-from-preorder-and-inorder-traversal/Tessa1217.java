import java.util.HashMap;
import java.util.Map;

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

    private Map<Integer, Integer> inorderIndexMap;
    private int preorderIndex = 0;

    public TreeNode buildTree(int[] preorder, int[] inorder) {

        inorderIndexMap = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            inorderIndexMap.put(inorder[i], i);
        }

        return buildTree(preorder, 0, inorder.length - 1);

    }

    private TreeNode buildTree(int[] preorder, int start, int end) {
        if (start > end) {
            return null;
        }

        int rootVal = preorder[preorderIndex++];
        // root 생성
        TreeNode root = new TreeNode(rootVal);

        int inorderIndex = inorderIndexMap.get(rootVal);

        // 분할 정복 방식으로 좌측과 우측 트리에 대한 정보 탐색
        // preorder의 0번째 = head
        // inorder 기준으로 봤을 때
        // root의 좌측은 좌측 서브트리, 우측은 우측 서브트리
        // 좌우측 서브트리를 각각 분할해서 탐색 진행
        // 분할한 preorder의 첫번째 노드 = 해당 트리의 head
        // depth 0 => head 3, left side => [9], right side => [15, 20, 7]
        // depth 1 => 
        //      left => head 9 => search node 더 이상 없음
        //      right => head 20 => left side => [15], right side => [7]
        //          depth 2 => 
        //              left => head 15 => 더는 탐색할 노드 없음
        //              right => head 7 => 더는 탐색할 노드 없음
        root.left = buildTree(preorder, start, inorderIndex - 1);
        root.right = buildTree(preorder, inorderIndex + 1, end);

        return root;
    }
}

