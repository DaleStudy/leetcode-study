// 시간 복잡도:  트리의 모든 노드를 한 번씩만 방문 -> O(n)
// 공간 복잡도: 재귀적으로 트리를 구성 ->
// 트리가 균형 잡힌 경우(즉, 트리의 높이가 log(n)인 경우), 재귀 호출 스택의 깊이는 O(log n)
// 트리가 편향된 형태(예: 모두 왼쪽 자식만 존재하는 경우)라면, 재귀 깊이는 O(n)

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
