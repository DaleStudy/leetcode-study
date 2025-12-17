/**
 * Runtime: 4ms
 * Time Complexity: O(n)
 *
 * Memory: 42.94MB
 * Space Complexity: O(n)
 *
 * Approach: 스택 사용
 * - 열린 괄호를 푸시하면서 닫힌 괄호가 나올 때마다 스택에서 팝하여 짝이 맞는지 확인
 */
class Solution {
    public boolean isValid(String s) {
        if (s.length()%2 == 1) return false;

        Stack<Character> stack = new Stack<>();
        Map<Character, Character> map = new HashMap<>();
        map.put('(', ')');
        map.put('{', '}');
        map.put('[', ']');

        for (char ch: s.toCharArray()) {
            if (map.containsKey(ch)) {
                stack.push(ch);
            } else if (")}]".indexOf(ch) != -1) {
                if (stack.isEmpty() || ch != map.get(stack.pop())) {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }
}
