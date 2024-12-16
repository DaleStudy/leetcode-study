
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {}

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {

    int preIdx = 0;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder == null || inorder == null || preorder.length == 0 || inorder.length == 0) {
            return null;
        }

        return build(preorder, inorder, 0, inorder.length - 1);
    }

    // O(n)
    private TreeNode build(int[] preorder, int[] inorder, int inStart, int inEnd) {
        // 재귀 종료 조건
        // 포인터(인덱스)가 배열 길이를 넘었을
        if (preIdx >= preorder.length || inStart > inEnd) {
            return null;
        }

        // preorder 첫 번째 값은 해당 부분 트리의 root 이다.
        int rootVal = preorder[preIdx++];
        TreeNode root = new TreeNode(rootVal);

        // inOrder 배열에서 root 값의 위치를 찾는다.
        int rootIndex = -1;
        for (int i = inStart; i <= inEnd; i++) {
            if (inorder[i] == rootVal) {
                rootIndex = i;
                break;
            }
        }

        // root 값을 기준으로 inorder 배열의 왼쪽 부분 배열(inStart ~ rootIndex-1)은 root의 left tree,
        // 오른쪽 부분 배열(rootIndex+1 ~ inEnd)은 root의 right tree 가 된다.
        root.left = build(preorder, inorder, inStart, rootIndex - 1);
        root.right = build(preorder, inorder, rootIndex + 1, inEnd);

        return root;
    }
}
