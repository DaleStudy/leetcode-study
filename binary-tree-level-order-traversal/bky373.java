/**
 * time: O(N)
 * space: O(N)
 */
class Solution {

    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if (root == null) {
            return result;
        }

        int level = 0;
        Queue<TreeNode> que = new LinkedList<TreeNode>();
        que.add(root);

        while (!que.isEmpty()) {
            result.add(new ArrayList<Integer>());

            int len = que.size();
            for (int i = 0; i < len; i++) {
                TreeNode cur = que.poll();
                result.get(level)
                      .add(cur.val);

                if (cur.left != null) {
                    que.add(cur.left);
                }
                if (cur.right != null) {
                    que.add(cur.right);
                }
            }
            level++;
        }
        return result;
    }
}
