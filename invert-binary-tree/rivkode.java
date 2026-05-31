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

 /*
1. 문제 이해

입력받은 이진트리를 insert하고 root 노드를 반환

2. 알고리즘

invert 하는 메서드를 만들어서 dfs 로 leaf 노드가 Null 일때까지 반복하자

3. 예외

4. 구현

dfs로 구현
dfs 에서 노드를 입력받고
좌우가 null 인지 판단
null 이라면 return
아니면 좌우를 Invert 시킨 뒤 다시 dfs 호출

놓쳤던 부분: 처음 root 노드에 대해서 Invert를 하지 않았다.


 */
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return root;
        }
        dfs(invert(root));

        return root;
    }

    public void dfs(TreeNode node) {
        if (node == null) {
            return;
        }
        if (node.left != null) {
            dfs(invert(node.left));
        }

        if (node.right != null) {
            dfs(invert(node.right));
        }
    }

    public TreeNode invert(TreeNode node) {
        TreeNode tmp;
        tmp = node.left;
        node.left = node.right;
        node.right = tmp;

        return node;
    }
}

