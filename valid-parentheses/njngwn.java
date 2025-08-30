// Time Complexity: O(n), n: s.length
// Space Complexity: O(n), n: s.length (worst case: s="(((((((")
class Solution {
    public boolean isValid(String s) {
        Stack<Character> bracketStack = new Stack<>();

        for (char ch : s.toCharArray()) {
            if (ch == '(' || ch == '{' || ch == '[') { // open bracket
                bracketStack.push(ch);
            } else {    // close bracket
                if (bracketStack.empty()) {
                    return false;
                }

                char sp = bracketStack.pop();
                if (!((sp == '(' && ch == ')') || (sp == '{' && ch == '}') || (sp == '[' && ch == ']'))) {
                    return false;
                }
            }
        }

        return bracketStack.empty();
    }
}
