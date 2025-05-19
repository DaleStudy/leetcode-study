import java.util.LinkedList;
import java.util.Queue;

// 시간복잡도 O(n)
class Solution {
    public int depth = 0;
    public int maxDepth(TreeNode root) {

        if(root == null) {
            return depth;
        }
        
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        while(!q.isEmpty()) {
            int size = q.size();
            depth++;

            for(int i = 0; i < size; i++) {
                TreeNode p = q.poll();

                if(p.right != null) {
                    q.add(p.right);
                }

                if(p.left != null) {
                    q.add(p.left);
                }
            }
        }

        return depth;
    }
}
