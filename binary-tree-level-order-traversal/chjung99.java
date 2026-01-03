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
        List<List<Integer>> answer = new ArrayList<>();
        Deque<Pair> queue = new ArrayDeque<>();
        int[] visit = new int[2000];
        if (root != null){
            queue.add(new Pair(root, 0));
        }

        while (!queue.isEmpty()) {
            Pair cur = queue.poll();
            // System.out.println(cur.node.val+ " depth="+cur.depth);
            if (visit[cur.depth] == 0){
                answer.add(new ArrayList<>());
                visit[cur.depth] = 1;
            }
            List<Integer> ls = answer.get(cur.depth);
            ls.add(cur.node.val);

            if (cur.node.left != null) queue.add(new Pair(cur.node.left, cur.depth + 1));
            if (cur.node.right != null) queue.add(new Pair(cur.node.right, cur.depth + 1));
        }
        return answer;
    }
    class Pair{
        TreeNode node;
        int depth;

        public Pair(TreeNode node, int depth){
            this.node = node;
            this.depth = depth;
        }
    }
}


