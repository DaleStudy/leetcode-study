/**
 * <a href="https://leetcode.com/problems/valid-parentheses/">week06-1.valid-parentheses</a>
 * <li>Description: determine if the input string is valid </li>
 * <li>Topics: String, Stack                    </li>
 * <li>Time Complexity: O(N), Runtime 2ms       </li>
 * <li>Space Complexity: O(N), Memory 41.98MB   </li>
 */

class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for(char c : s.toCharArray()) {
            if(isOpenBracket(c)){
                stack.push(c);
                continue;
            }

            if(stack.isEmpty() || isNoneMatchBracket(stack.pop(), c)) {
                return false;
            }
        }

        return stack.isEmpty();
    }

    private boolean isOpenBracket(char open) {
        return open == '(' || open == '{' || open == '[';
    }

    private boolean isNoneMatchBracket(char open, char close) {
        if(open == '(') return close != ')';
        if(open == '{') return close != '}';
        if(open == '[') return close != ']';
        return true;
    }
}
