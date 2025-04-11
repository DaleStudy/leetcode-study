// time: O(n)
class Solution {
    func isValidBST(_ root: TreeNode?) -> Bool {
        return checkNodes(root, Int.min, Int.max)
    }

    func checkNodes(_ root: TreeNode?, _ min: Int, _ max: Int) -> Bool {
        guard let node = root else { return true }
        if node.val <= min || node.val >= max { return false }

        return checkNodes(node.left, min, node.val) && checkNodes(node.right, node.val, max)
    }
}
/*
 중위순회를 통해서도 해결이 가능하다.
 중위순회를 하며 이전에 들렀던 값보다 현재 방문한 노드의 값이 작으면 false!
*/
