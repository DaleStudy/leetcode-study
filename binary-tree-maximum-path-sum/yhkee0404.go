/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxPathSum(root *TreeNode) int {
    ans, _ := solve(root)
    return ans
}

func solve(root *TreeNode) (int, int) {
    if root == nil {
        return -30_000_000, -30_000_000
    }
    leftAns, leftRootAns := solve(root.Left)
    rightAns, rightRootAns := solve(root.Right)
    rootAns := root.Val + max(0, leftRootAns, rightRootAns,)
    ans := max(leftAns, rightAns, root.Val + max(0, leftRootAns,) + max(0, rightRootAns,))
    return ans, rootAns
}
