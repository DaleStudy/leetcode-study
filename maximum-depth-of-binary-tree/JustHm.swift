// time: O(n) space: O(n)
class Solution {
    func maxDepth(_ root: TreeNode?) -> Int {
        return dfs(root, 1)
    }

    func dfs(_ node: TreeNode?, _ n: Int) -> Int {
        guard let node = node else { return n - 1 }
        return max(dfs(node.left, n+1), dfs(node.right, n+1))
    }
}
