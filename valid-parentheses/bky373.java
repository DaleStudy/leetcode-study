/**
 * - 문제: https://leetcode.com/problems/valid-parentheses/
 * - TC: O(N)
 * - SC: O(1)
 */
class Solution_20 {

    public boolean isValid(String s) {
        Stack<Character> st = new Stack<>();
        Map<Character, Character> pairs = Map.of('(', ')', '{', '}', '[', ']');

        for (int i = 0; i < s.length(); i++) {
            // 열린 괄호이면 스택에 push
            if (pairs.containsKey(s.charAt(i))) {
                st.push(s.charAt(i));
            } else { // 닫힌 괄호인데
                if (st.isEmpty()) { // 스택이 비어있으면(열린 괄호가 없으면) false 반환
                    return false;
                }
                // 스택의 최근 요소(열린 괄호)와 짝을 이루지 않으면 false 반환
                if (s.charAt(i) != pairs.get(st.pop())) {
                    return false;
                }
            }
        }
        // 열린 괄호가 남아 있을 수 있으므로 목록이 비어있는지 체크
        return st.isEmpty();
    }
}
