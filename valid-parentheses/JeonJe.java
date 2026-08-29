import java.util.*;

// TC: O(n)
// SC: O(n)
class Solution {
    private static final Map<Character, Character> PAIRS = Map.of(
            ')', '(',
            ']', '[',
            '}', '{'
    );

    public boolean isValid(String s) {

        ArrayDeque<Character> stack = new ArrayDeque<>();

        for (char c : s.toCharArray()) {
            if (!PAIRS.containsKey(c)) {
                stack.push(c);
                continue;
            }

            if (!PAIRS.get(c).equals(stack.peek())) {
                return false;
            }
            stack.pop();
        }
        return stack.isEmpty();
    }
}
