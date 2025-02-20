/**
 이 문제는 힌트의 도움을 받아서 풀었습니다.
 - preorder의 첫 원소는 항상 root node임
 - inorder에서 root node의 왼쪽의 원소들은 root node의 왼쪽 subtree, 오른쪽 원소들은 오른쪽 subtree임
 - 왼쪽 subtree와 오른쪽 subtree는 각각 preorder에서 연속하게 있음. (root, 왼쪽 subtree, 오른쪽 subtree 순)

 시간 복잡도 : O(n)
 공간 복잡도 : O(n^2)
 (skewed tree의 경우, 최악의 공간 복잡도를 가짐)
 */
class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder.length == 0) {
            return null;
        }
        if (preorder.length == 1) {
            return new TreeNode(preorder[0]);
        }
        int currIdx;
        for (currIdx = 0; currIdx < inorder.length; currIdx++) {
            if (inorder[currIdx] == preorder[0]) {
                break;
            }
        }

        int[] lp = new int[currIdx];
        int[] li = new int[currIdx];
        int[] rp = new int[inorder.length - currIdx - 1];
        int[] ri = new int[inorder.length - currIdx - 1];
        for (int i = 0; i < currIdx; i++) {
            lp[i] = preorder[i + 1];
            li[i] = inorder[i];
        }
        for (int i = currIdx + 1; i < inorder.length; i++) {
            rp[i - currIdx - 1] = preorder[i];
            ri[i - currIdx - 1] = inorder[i];
        }

        TreeNode lc = buildTree(lp, li);
        TreeNode rc = buildTree(rp, ri);

        TreeNode curr = new TreeNode(preorder[0], lc, rc);

        return curr;
    }
}
