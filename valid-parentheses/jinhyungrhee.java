import java.util.*;
class Solution {
    /**
     * time-complexity : O(n)
     * space-complexity : O(n)
     */
    public boolean isValid(String s) {

        Deque<Character> stack = new ArrayDeque<>();
        Map<Character, Character> table = new HashMap<>();
        table.put(')', '(');
        table.put(']', '[');
        table.put('}', '{');

        for (int i = 0; i < s.length(); i++) {
            if (table.containsKey(s.charAt(i))) {

                if ((table.get(s.charAt(i))).equals(stack.peek())) {
                    stack.pop();
                } else {
                    stack.push(s.charAt(i));
                }

            } else {
                stack.push(s.charAt(i));
            }
        }

        return stack.isEmpty();
    }
}
