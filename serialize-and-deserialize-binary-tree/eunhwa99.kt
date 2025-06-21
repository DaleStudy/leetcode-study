package leetcode_study

class Codec {
    private var index = 0
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    fun serialize(root: TreeNode?): String {
        return buildString {
            traverse(root, this)
        }
    }

    fun traverse(node: TreeNode?, sb: StringBuilder) {
        if (node == null) {
            sb.append("null,")
            return
        }
        sb.append("${node.`val`},")
        traverse(node.left, sb)
        traverse(node.right, sb)
    }

    // Time Complexity: O(n)
    // Space Complexity: O(n)
    fun deserialize(data: String): TreeNode? {
        val values = data.split(",").filter { it.isNotEmpty() }.toList()
        index = 0
        return buildTree(values)
    }

    fun buildTree(values: List<String>): TreeNode? {
        if (index >= values.size) return null
        val value = values[index++] // index 는 매개변수가 아니라 전역으로 두어야 한다!!
        if (value == "null") return null
        val node = TreeNode(value.toInt())
        node.left = buildTree(values)
        node.right = buildTree(values)
        return node
    }
}

