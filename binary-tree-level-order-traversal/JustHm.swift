// 재귀 함수로 해결
// 각 노드의 레벨을 기억하고있다가 정답변수에 레벨별로 노드값을 넣어줌
class Solution {
    func levelOrder(_ root: TreeNode?) -> [[Int]] {
        var answer = [[Int]]()
        searchNodes(0, root, &answer)
        return answer
    }

    func searchNodes(_ level: Int, _ node: TreeNode?, _ answer: inout [[Int]]) {
        guard let node else { return }
        if level >= answer.count { answer.append([]) }
        answer[level].append(node.val)
        searchNodes(level + 1, node.left, &answer)
        searchNodes(level + 1, node.right, &answer)
    }
}
