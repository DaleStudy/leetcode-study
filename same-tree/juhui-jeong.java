/**
 * 시간복잡도: O(n)
 * 공간복잡도: O(h)
 */
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;
        if (p == null || q == null) return false;
        if (p.val != q.val) return false;
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}

class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        Queue<TreeNode> queueP = new LinkedList<>();
        Queue<TreeNode> queueQ = new LinkedList<>();

        queueP.offer(p);
        queueQ.offer(q);

        while(!queueP.isEmpty() && !queueQ.isEmpty()) {
            TreeNode curP = queueP.poll();
            TreeNode curQ = queueQ.poll();

            if (curP == null && curQ == null) continue;
            if (curP == null || curQ == null) return false;

            if (curP.val != curQ.val) return false;

            queueP.offer(curP.left);
            queueQ.offer(curQ.left);
            queueP.offer(curP.right);
            queueQ.offer(curQ.right);            
        }
        return true;
    }
}
