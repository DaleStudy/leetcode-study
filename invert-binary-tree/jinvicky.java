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
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;

        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;

        System.out.println(root.val);

        invertTree(root.left);
        invertTree(root.right);

        return root;
    }

    public TreeNode invertTreeByQueue(TreeNode root) {
        if (root == null) {
            return null;
        }

        // BFS를 위한 큐 생성
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        // 큐가 빌 때까지 반복
        while (!queue.isEmpty()) {
            TreeNode current = queue.poll();

            // 현재 노드의 왼쪽 자식과 오른쪽 자식 교환
            TreeNode temp = current.left;
            current.left = current.right;
            current.right = temp;

            // 자식 노드가 있으면 큐에 추가
            if (current.left != null) {
                queue.add(current.left);
            }
            if (current.right != null) {
                queue.add(current.right);
            }
        }

        return root;
    }
}
/**
 * public TreeNode invertTreeByQueue(TreeNode root) {
 * 	// root가 널이면 리턴
 * 	// 큐 선언하고 루트를 삽입
 *
 * 	// 큐가 비기 전까지 연산 반복
 * 		// temp 변수로 left와 right을 교체
 * 		// 자식 left 노드를 큐에 추가 (있다면)
 * 		// 자식 right 노드를 큐에 추가 (있다면)
 * 	// 루트를 반환
 * }
 */
