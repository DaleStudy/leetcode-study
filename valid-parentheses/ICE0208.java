import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        Map<Character, Character> mapping = new HashMap<>();
        mapping.put(')', '(');
        mapping.put('}', '{');
        mapping.put(']', '[');

        for (Character c : s.toCharArray()) {
            // 열린 괄호일 때, 스택에 push
            if (c=='(' || c=='{' || c == '[') {
                stack.push(c);
                continue;
            }

            // 닫힌 괄호일 때, 스택에서 pop한 뒤, 비교
            // 스택이 비어있으면 탈락
            if (stack.isEmpty()) {
                return false;
            }
            Character popedC = stack.pop();
            Character target = mapping.get(c);
            // 같은 종류의 괄호가 아니면 탈락
            if (!target.equals(popedC)) {
                return false;
            }
        }
        
        // 마지막에 스택이 비어있어야 성공
        return stack.isEmpty();
    }
}
