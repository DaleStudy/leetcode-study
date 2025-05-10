class Solution {
    public boolean isValid(String s) {
        Stack<Character> checking = new Stack<>();

        for(char c : s.toCharArray()){
            if(c == '(' || c == '{' || c == '['){
                checking.push(c);
                continue;
            }
            if(checking.empty()) return false;

            if(c == ')' && checking.peek() == '('){
                checking.pop();
                continue;
            }
            if(c == '}' && checking.peek() == '{'){
                checking.pop();
                continue;
            }
            if(c == ']' && checking.peek() == '['){
                checking.pop();
                continue;
            }
            return false;
        }
        if(!checking.empty()) return false;
        return true;
    }
}

