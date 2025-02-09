package leetcode_study

/**
 * 시간복잡도 : O(n)
 * 문자를 하나씩 돌면서 스택에 추가 또는 확인하는 알고리즘이기 때문에 O(n) 입니다.
 *
 * 공간복잡도 : O(n)
 * 문자가 모두 여는 형태의 괄호일 때, 스택의 길이는 최대 n 이므로 O(n) 입니다.
 * */
fun isValid(s: String): Boolean {
    val chars = s.toCharArray()
    val stack = ArrayDeque<Char>()

    val pairs = hashMapOf(
        '(' to ')',
        '{' to '}',
        '[' to ']'
    )

    val openers = setOf('(', '[', '{')
    val closers = setOf(')', ']', '}')

    chars.forEach { char ->
        when (char) {
            in openers -> {
                stack.add(char)
            }
            in closers -> {
                if (stack.isEmpty()) return false

                val recentOpener = stack.removeLast()
                if (pairs[recentOpener] != char) return false
            }
        }
    }

    return stack.isEmpty()
}
