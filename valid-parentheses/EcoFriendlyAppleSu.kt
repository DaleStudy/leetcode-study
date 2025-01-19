package leetcode_study

/*
* Pair Bracket 판별 문제
* 스택의 LIFO의 성질을 사용해 문제 해결
* 시간 복잡도: O(n)
* -> 문자열 길이만큼 반복 진행: O(n)
* 공간 복잡도: O(n)
* -> 주어진 문자열 길이만큼 공간 필요: O(n)
* */
fun isValid(s: String): Boolean {
    val stack = mutableListOf<Char>()

    for (element in s) {
        if (element == ')' || element == ']' || element == '}') {
            if (stack.isEmpty()) {
                return false
            } else if (stack.last() == '(' && element == ')') {
                stack.removeAt(stack.lastIndex)
            } else if (stack.last() == '[' && element == ']') {
                stack.removeAt(stack.lastIndex)
            } else if (stack.last() == '{' && element == '}') {
                stack.removeAt(stack.lastIndex)
            } else {
                return false
            }
        } else {
            stack.add(element)
        }
    }
    return stack.isEmpty()
}
