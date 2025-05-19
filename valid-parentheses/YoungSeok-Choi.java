import java.util.Stack;

// TC: O(n)
class Solution {
    Stack<Character> st = new Stack<>();
    public boolean isValid(String s) {
        for(char c : s.toCharArray()) {
            if(st.empty() || !isClosing(c)) {
                st.push(c);
                continue;
            }

            char temp = st.peek();
            if(temp == '(' && c == ')') {
               st.pop(); 
            } else if(temp == '[' && c == ']') {
               st.pop();
            } else if(temp == '{' && c == '}') {
                st.pop();
            } else {
                st.push(c);
            }
        }

        return st.empty();
    }

    public boolean isClosing(char c) {
        if(c == ')' || c == ']' || c == '}') return true;

        return false;
    }
}
