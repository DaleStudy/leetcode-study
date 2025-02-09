package leetcode_study

class Solution {
    /** 시간 : O(n), 공간 : O(n) */
    fun isValid(s: String): Boolean {
        val stack = Stack<Char>()
        val openParentheses = "([{"
        s.forEach {
            if (openParentheses.contains(it)) {
                stack.push(it)
            } else {
                if (stack.isEmpty()) {
                    return false
                }
                val top = stack.pop()
                if (
                    top == openParentheses[0] && it != ')' ||
                    top == openParentheses[1] && it != ']' ||
                    top == openParentheses[2] && it != '}'
                ) {
                    return false
                }
            }
        }
        return stack.isEmpty()
    }
}
