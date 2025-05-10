/**
[문제풀이]
- 열린 괄호에 대한 스택을 쌓으면 어떨까?
- 닫는 괄호가 중요하니까 닫히는걸 쌓아보자.
time: O(N), space: O(N)

[회고]
분기처리가 보기 싫게 되어 있는데 Map으로 하면 좋을까? 오히려 공간을 더 쓰게 되는건 아닐까?
실무라면 쓸 것 같다.
 */
class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (char c: s.toCharArray()) {
            if (c == '(') {
                stack.push(')');
            } else if (c == '{') {
                stack.push('}');
            } else if (c == '[') {
                stack.push(']');
            } else {
                if (stack.isEmpty() || stack.pop() != c) {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}

