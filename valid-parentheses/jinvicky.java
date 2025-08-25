import java.util.Stack;

class Solution {
    /**
     * 주어진 문자열 s의 괄호가 제대로 닫혀있는지 여부를 판단하는 문제입니다.
     * 나올 수 있는 괄호의 종류는 3개이며 짝맞추기에 유리한 자료구조인 스택을 사용합니다.
     * {, [, ( 같은 왼쪽 괄호는 무조건 stack에 추가됩니다.
     * }, ], ) 같은 오른쪽 괄호를 만나면 매칭되는 왼쪽 괄호를 만날 때까지 pop()을 통해 stack에서 괄호들을 꺼내야 합니다.
     */
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else {
                /**
                 * [중요] 문자열이 오른쪽 괄호로만 구성되는 경우도 있으므로 for문이 반복되는데 스택이 비었다면
                 * 그 즉시 false를 반환하고 break해야만 stack Exception을 막을 수 있습니다.
                 * 문제 케이스: "]"
                 */
                if (stack.isEmpty()) {
                    return false;
                }
                if (stack.peek() == '(' && c == ')') {
                    stack.pop();
                } else if (stack.peek() == '[' && c == ']') {
                    stack.pop();
                } else if (stack.peek() == '{' && c == '}') {
                    stack.pop();
                }
            }
        }
        return stack.isEmpty(); // 스택이 비었다면 괄호는 짝이 맞는다는 의미입니다.
    }
}
