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
    public List<List<Integer>> levelOrder(TreeNode root) {
        /**
        1.문제: 레벨순으로 왼쪽에서 오른쪽으로 노드 순회
        2.constraints: num of nodes min = 0, max = 2000
        3.solution: bfs, queue
        -time complexity: O(n) - 노드 수
        -space complexity: O(n) - 전체 노드를 저장하므로 
         */
         List<List<Integer>> answer = new ArrayList<>();

         if(root == null) {
            return new ArrayList<>();
         }

         Queue<TreeNode> q = new LinkedList<>();
         q.offer(root);

         while(!q.isEmpty()) {
            int size = q.size();
            //동일한 레벨 노드 값들을 담을 리스트
            List<Integer> currentLevel = new ArrayList<>();

            for(int i = 0; i < size; i++) {
                TreeNode node = q.poll();
                currentLevel.add(node.val);

                if(node.left != null) {
                    q.offer(node.left);
                }
                if(node.right != null) {
                    q.offer(node.right);
                }
            }
            answer.add(currentLevel);
         }
        return answer;
    }
}
