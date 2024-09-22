// TC: O(n)
// -> n = s.length
// SC: O(n)
// -> n = s.length / 2
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            if (c == '(') stack.add(')');
            else if (c == '{') stack.add('}');
            else if (c == '[') stack.add(']');
            else if (stack.isEmpty() || stack.pop() != c) return false;
        }

        return stack.isEmpty();
    }
}
