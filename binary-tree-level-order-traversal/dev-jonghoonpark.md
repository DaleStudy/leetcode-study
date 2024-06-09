- 문제: https://leetcode.com/problems/binary-tree-level-order-traversal/
- time complexity : O(n)
- space complexity : O(n), 트리가 균등한 형태일 경우 O(logn)에 가까워진다. (결과에 사용되는 list는 고려하지 않는다.)
- 블로그 링크 : https://algorithm.jonghoonpark.com/2024/06/10/leetcode-102

```java
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();

        dfs(result, root, 0);

        return result;
    }

    public void dfs(List<List<Integer>> result, TreeNode node, int level) {
        if(node == null) {
            return;
        }

        if (result.size() <= level) {
            result.add(new ArrayList<>());
        }
        result.get(level).add(node.val);

        dfs(result, node.left, level + 1);
        dfs(result, node.right, level + 1);
    }
}
```
