import java.util.*;

class Solution {
    public boolean isValid(String s) {
        ArrayDeque<Character> stack = new ArrayDeque<>();
        for (int i = 0; i < s.length(); i++){
            if (s.charAt(i) == '(' || s.charAt(i) == '{' || s.charAt(i) == '[' ){
                stack.push(s.charAt(i));
                continue;
            }

            if (s.charAt(i) == ')' && !stack.isEmpty() && stack.peek() == '('){
                stack.pop();
                continue;
            }

            if (s.charAt(i) == '}' && !stack.isEmpty() && stack.peek() == '{'){
                stack.pop();
                continue;
            }

            if (s.charAt(i) == ']' && !stack.isEmpty() && stack.peek() == '['){
                stack.pop();
                continue;
            }
            return false;
        }
        return stack.isEmpty();

    }
}
