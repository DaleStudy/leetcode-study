import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

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