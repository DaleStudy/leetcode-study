/**
 input : string s contains just (, ), {, }, [, ]
 output : return if s is valid
 valid means that parentheses are matched(balanced)
 example
 ((())) : valid
 (((())) : invalid
 {() : invalid

 constraint :
 1) input string can be empty string?
 nope. at least one character  >> if length is odd number return false
 edge:
 1) if the length of string is odd number return false

 solution 1)
 ds : stack
 algo : x
 iterate through the string s
 if opening bracket, add to stack
 else check the top element of stack
 if matched pop
 else return false;
 return false

 tc : O(n)
 sc : O(n) worst case : every character is opening bracket

 */
class Solution {
  public boolean isValid(String s) {
    //edge
    if(s.length() % 2 == 1) return false;
    // we can use deque instead
    Stack<Character> stack = new Stack<>();

    for(char c : s.toCharArray()) {
      if(c == '(' || c == '{' || c == '[') {
        stack.push(c);
      } else {
        if(stack.isEmpty()) return false;
        if(c == ')') {
          if(stack.peek() != '(') return false;
        } else if (c == '}') {
          if(stack.peek() != '{') return false;
        } else if (c == ']'){
          if(stack.peek() != '[') return false;
        }
        stack.pop();
      }
    }
    return stack.isEmpty();
  }
}
