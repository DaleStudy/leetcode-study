class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();

        for(char c : s.toCharArray()) {
            if(c == '(' || c=='{' || c=='[') {
                stack.push(c);
            }
            if(c == ')') {
                if(stack.isEmpty() || stack.peek() != '(') return false;
                 stack.pop();
            }
            if(c == '}') {
                if(stack.isEmpty() || stack.peek() != '{') return false;
                stack.pop();
            }
            if(c == ']') {
                if(stack.isEmpty() || stack.peek() != '[') return false;
                stack.pop();    
            }
        }
        return stack.isEmpty();
    }
}


