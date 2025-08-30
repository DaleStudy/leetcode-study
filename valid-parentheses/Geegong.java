import java.util.HashMap;
import java.util.Stack;

public class Geegong {

    /**
     * stack 자료구조 사용
     * 닫는 부분만 hashMap의 key 값으로 서로 페어가 되는 값을 value 로 한다.
     * stack 자료구조는 닫는 bracket이 아니면 push 해서 넣고 닫는 bracket 만 체크를 하는데
     * stack 에서 pop 을 하는데 이떄 map의 value와 다르면 false
     *
     * time complexity : o(n)
     * space complexity : o(1)
     * @param s
     * @return
     */
    public boolean isValid(String s) {
         HashMap<Character, Character> map = new HashMap<Character, Character>();
         map.put(')', '(');
         map.put(']', '[');
         map.put('}', '{');

         Stack<Character> stack = new Stack<Character>();
         for (int i=0; i<s.length(); i++) {
             Character ch = s.charAt(i);
             if (map.containsKey(ch)) {
                 if (stack.isEmpty() || map.get(ch) != stack.pop()) {
                     return false;
                 }
             } else {
                 stack.push(ch);
             }
         }

         return stack.isEmpty();
    }
}

