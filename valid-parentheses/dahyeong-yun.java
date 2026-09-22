/**
  * TC : O(n)
  *   - 문자열 s의 길이 만큼 순회 하므로 O(n)
  * SC : O(n)
  *   - 문자열 길이 만큼의 char 배열을 생성하고, 최대 n/2 만큼의 스택 사용. 합산 1.5n 이므로 O(n)
  */
class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();

        for(char c : s.toCharArray()) {
            //여는 괄호의 경우 stack 에 쌓기
            if(c == '{'
            || c == '('
            || c == '['
            ) {
                stack.push(c);
            } else {
            // 닫는 괄호의 경우 stack이 비어있으면 안됨
                if(stack.size() < 1) return false;
                else {
                    char peek = stack.peek();
                    if((peek == '(' && c == ')') 
                    || (peek == '{' && c == '}') 
                    || (peek == '[' && c == ']')
                    ) {
                        stack.pop();
                    } else {
                        return false;
                    }
                }
            }
        }

        return stack.size() == 0;
    }
}
