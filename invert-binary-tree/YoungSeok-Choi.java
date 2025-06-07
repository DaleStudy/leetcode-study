import java.util.HashMap;
import java.util.Map;

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
}

// tc -> O(n)
class Solution {

    public TreeNode invertTree(TreeNode root) {
        if (root == null)
            return null;

        TreeNode left = invertTree(root.left);
        TreeNode right = invertTree(root.right);

        root.right = left;
        root.left = right;

        return root;
    }

}

// NOTE: deep copy 작업도 해볼 것
// 같은 val의 Node가 여러 개 들어오는 경우를 고려하지 못했음..
class WrongSolution {

    public Map<Integer, TreeNode> tMap = new HashMap<>();

    public TreeNode invertTree(TreeNode root) {
        if (root == null)
            return null;

        int rVal = root.val;

        tMap.computeIfAbsent(rVal, k -> new TreeNode(k));

        TreeNode cur = tMap.get(rVal);

        if (root.left != null) {
            tMap.computeIfAbsent(root.left.val, k -> new TreeNode(k));
            cur.right = tMap.get(root.left.val);
            invertTree(root.left);
        }

        if (root.right != null) {
            tMap.computeIfAbsent(root.right.val, k -> new TreeNode(k));
            cur.left = tMap.get(root.right.val);
            invertTree(root.right);
        }

        return tMap.get(root.val);
    }
}
