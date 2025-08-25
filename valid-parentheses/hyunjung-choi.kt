/**
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(n)
 */

class Solution {
    fun isValid(s: String): Boolean {
        if (s.length % 2 == 1) return false

        val stack = Stack<Char>()
        val pairs = mapOf(')' to '(', ']' to '[', '}' to '{')

        for (char in s) {
            when {
                char in pairs -> {
                    if (stack.isEmpty() || stack.pop() != pairs[char]) {
                        return false
                    }
                }

                else -> stack.push(char)
            }
        }

        return stack.isEmpty()
    }
}
