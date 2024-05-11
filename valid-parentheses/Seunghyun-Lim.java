/**
 * 시간복잡도: O(n)
 * -> 문자열 s의 길이에 따라 증가
 * 공간복잡도: O(n)
 * -> 문자열 s의 길이에 따라 stack의 공간 증가
 */
class Solution {
    public boolean isValid(String s) {
        char first = s.charAt(0);
        if (s.length() == 1 || first == ')' || first == '}' || first == ']') return false;

        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
                continue;
            }

            if (stack.isEmpty()) return false;

            if (c == ')') {
                Character pop = stack.pop();
                if (pop != '(') return false;
            } else if (c == '}') {
                Character pop = stack.pop();
                if (pop != '{') return false;
            } else if (c == ']') {
                Character pop = stack.pop();
                if (pop != '[') return false;
            }
        }

        return stack.size() == 0;
    }
}
