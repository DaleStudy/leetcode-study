import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
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

    // DFS 풀이
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        dfs(root, 0, result);
        return result;
    }

    private void dfs(TreeNode node, int depth, List<List<Integer>> result) {
        if (node == null) {
            return;
        }

        // 깊이만큼의 리스트가 없으면 새 리스트 추가하기
        if (depth == result.size()) {
            result.add(new ArrayList<>());
        }

        result.get(depth).add(node.val);

        dfs(node.left, depth + 1, result);
        dfs(node.right, depth + 1, result);


    }

    // BFS로 풀이
    // O(n)
//    public List<List<Integer>> levelOrder(TreeNode root) {
//
//        List<List<Integer>> result = new ArrayList<>();
//
//        if (root == null) {
//            return result;
//        }
//
//        Queue<TreeNode> queue = new LinkedList<>();
//        queue.offer(root);
//
//        while (!queue.isEmpty()) {
//            int nodeCnt = queue.size();
//            List<Integer> currentLevelNodes = new ArrayList<>();
//
//            for (int i = 0; i < nodeCnt; i++) {
//                TreeNode current = queue.poll();
//                currentLevelNodes.add(current.val);
//
//                if (current.left != null) {
//                    queue.offer(current.left);
//                }
//
//                if (current.right != null) {
//                    queue.offer(current.right);
//                }
//
//            }
//
//            result.add(currentLevelNodes);
//
//        }
//
//        return result;
//
//    }
}

