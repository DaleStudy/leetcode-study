package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test
import java.util.StringJoiner

/**
 * 문제의 핵심은 트리를 탐색하는 순서 기준으로 직렬화된 문자열을 반대로 풀어내는 것
 * 직렬화를 DFS로 해결하면 역직렬화시 선입선출 방식으로 해결하여야 하고,
 * 직렬화를 BFS로 해결하면 역직렬화시 힙의 인덱스 규칙을 이용하여 해결할 수 있을 듯
 */
class `serialize-and-deserialize-binary-tree` {

    private val empty = "X"
    private val delimiter = "|"

    /**
     * DFS로 탐색하면서 노드의 값을 누적한다.
     * TC: O(n), SC: O(n)
     */
    fun serialize(root: TreeNode?): String {
        if (root == null) return ""

        val joiner = StringJoiner("|")
        nodeToString(root, joiner)
        return joiner.toString()
    }

    private fun nodeToString(node: TreeNode?, joiner: StringJoiner) {
        if (node == null) {
            joiner.add(empty)
        } else {
            joiner.add(node.`val`.toString())
            nodeToString(node.left, joiner)
            nodeToString(node.right, joiner)
        }
    }

    /**
     * 깊이 탐색으로 누적된 문자열을 선입선출로 꺼내어 노드를 생성한다.
     * TC: O(n), SC: O(n)
     */
    fun deserialize(data: String): TreeNode? {
        if (data.isEmpty()) return null
        return stringToNode(ArrayDeque(data.split(delimiter)))
    }

    private fun stringToNode(queue: ArrayDeque<String>): TreeNode? {
        val value = queue.removeFirst()
        return if (value == empty) {
            null
        } else {
            val node = TreeNode(value.toInt())
            node.left = stringToNode(queue)
            node.right = stringToNode(queue)
            node
        }
    }

    @Test
    fun `트리 노드를 직렬화한다`() {
        serialize(TreeNode.of(1,2,3,null,null,4,5)) shouldBe "1|2|X|X|3|4|X|X|5|X|X"
    }

    @Test
    fun `문자열을 트리 노드로 역직렬화한다`() {
        deserialize("1|2|X|X|3|4|X|X|5|X|X") shouldBe TreeNode.of(1,2,3,null,null,4,5)
    }
}
