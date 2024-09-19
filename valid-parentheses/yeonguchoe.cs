public class Solution {
    public bool IsValid(string s) {
        Stack<char> parentheses = new Stack<char>();
        
        Dictionary<char, char> pair = new Dictionary<char, char> {
            { ')', '(' },
            { '}', '{' },
            { ']', '[' }
        };

        foreach (char c in s) {
            if (c == '(' || c == '{' || c == '[') {
                parentheses.Push(c);
            } 
            else if (c == ')' || c == '}' || c == ']') {
                if (parentheses.Count == 0 || parentheses.Peek() != pair[c]) {
                    return false;
                }
                parentheses.Pop();
            }
        }

        return parentheses.Count == 0;
    }
