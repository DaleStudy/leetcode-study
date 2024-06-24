- https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
- time complexity : O(n)
- space complexity : O(n)
- https://algorithm.jonghoonpark.com/2024/06/23/leetcode-105

```java
class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        Map<Integer, Integer> inorderIndexMap = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            inorderIndexMap.put(inorder[i], i);
        }

        return buildTree(inorderIndexMap, new Traversal(preorder), new Traversal(inorder));
    }

    public TreeNode buildTree(Map<Integer, Integer> inorderIndexMap, Traversal preorderTraversal, Traversal inorderTraversal) {
        if(preorderTraversal.start > preorderTraversal.end) {
            return null;
        }

        TreeNode treeNode = new TreeNode(preorderTraversal.getFirst());
        if(preorderTraversal.start == preorderTraversal.end) {
            return treeNode;
        }

        int rootIndex = inorderIndexMap.get(preorderTraversal.getFirst());
        int leftSize = rootIndex - inorderTraversal.start;
        treeNode.left = buildTree(
                inorderIndexMap,
                preorderTraversal.subIterator(preorderTraversal.start + 1, preorderTraversal.start + leftSize),
                inorderTraversal.subIterator(inorderTraversal.start, rootIndex - 1)
        );
        treeNode.right = buildTree(
                inorderIndexMap,
                preorderTraversal.subIterator(preorderTraversal.start + leftSize + 1, preorderTraversal.end),
                inorderTraversal.subIterator(rootIndex + 1, inorderTraversal.end)
        );

        return treeNode;
    }
}

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

    @Override
    public String toString() {
        return "{" +
                "val=" + val +
                ", left=" + left +
                ", right=" + right +
                '}';
    }
}

class Traversal {
    int[] array;
    int start;
    int end;

    public Traversal(int[] array) {
        this.array = array;
        this.start = 0;
        this.end = array.length - 1;
    }

    private Traversal(int[] array, int start, int end) {
        this.array = array;
        this.start = start;
        this.end = end;
    }

    public Traversal subIterator(int start, int end) {
        return new Traversal(array, start, end);
    }

    public int getFirst() {
        return array[start];
    }

    public Traversal(int start, int end) {
        this.start = start;
        this.end = end;
    }

    @Override
    public String toString() {
        return "{" +
                "start=" + start +
                ", end=" + end +
                '}';
    }
}
```
