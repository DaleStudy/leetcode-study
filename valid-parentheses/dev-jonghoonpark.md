- https://leetcode.com/problems/valid-parentheses/
- time complexity : O(n)
- space complexity : O(n)
- https://algorithm.jonghoonpark.com/2024/04/29/leetcode-20

```java
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
                continue;
            }

            if (stack.isEmpty()) {
                return false;
            }

            boolean valid = false;
            if (c == ')') {
                valid = stack.peek() == '(';
            } else if (c == '}') {
                valid = stack.peek() == '{';
            } else if (c == ']') {
                valid = stack.peek() == '[';
            }

            if (valid) {
                stack.pop();
            } else {
                return false;
            }
        }

        return stack.isEmpty();
    }
}
```
