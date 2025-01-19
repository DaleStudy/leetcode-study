class Solution {
    public boolean isValid(String s) {
        /**
        1. understanding
        - given string contains character which has paired characters.
        - validate all given characters in input string has each pair, and valid in order.
        2. strategy
        - use stack, to save left brackets, and if you encounter right bracket, then pop from stack, and compare two characters are paired.
        - if not paired on any right character, or stack is empty then return false.
        - all characters are iterated and stack is not empty, then return false.
        3. complexity
        - time: O(N), N is the length of input string s.
        - space: O(N), for stack variable memory.
        */
        Stack<Character> leftBracket = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                // when character is left bracket, then push to stack.
                leftBracket.push(c);
            } else if (c == ')' || c == '}' || c == ']') {
                if (leftBracket.isEmpty()) return false;
                char left = leftBracket.pop();
                if (isPair(left, c)) continue;
                return false;
            } else {
                throw new RuntimeException(String.format("Not valid input character: %c in input %s", c, s));
            }
        }
        return leftBracket.isEmpty();
    }

    private boolean isPair(char left, char right) {
        return (left == '(' && right == ')') 
            || (left == '{' && right == '}')
            || (left == '[' && right == ']');
    }
}

