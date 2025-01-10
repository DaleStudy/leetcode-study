import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

// 열린 괄호일 경우. 스택에 푸쉬
// 닫힌 괄호일 경우, 스택의 top 부분이 같은 종류의 열린 괄호이면 pop, 다른 종류 열린 괄호이면 invalid한 문자열

// 시간 복잡도: 스택의 크기 = 문자열의 크기 O(N)
// 공간 복잡도: 스택의 크기 = O(N)
class Solution {
    public boolean isValid(String s) {
        char[] array = s.toCharArray();
        Map<Character, Character> pMap = new HashMap<>();
        pMap.put(')','(');
        pMap.put('}','{');
        pMap.put(']','[');

        Stack<Character> stack = new Stack<>();
        for(char parenthes: array){
             if((parenthes == ')') || (parenthes=='}') || (parenthes==']')){
                if(stack.isEmpty()) return false; // invalid
                
                char myPair = pMap.get(parenthes);
                if(stack.peek()==myPair){
                    stack.pop();
                }
                else return false;
            }
            else{
                stack.push(parenthes);
            }
        }
        
        return stack.empty();
    }
}
